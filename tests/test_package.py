"""Contract tests; all mutations stay in scratch, never installed skills."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / 'scripts/check_package.py'

class PackageTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(CHECKER.exists(), 'checker is not implemented yet')
        spec = importlib.util.spec_from_file_location('checker', CHECKER)
        assert spec is not None and spec.loader is not None
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.copy = Path(self.tmp.name) / 'apple-inspired-frontend'
        shutil.copytree(ROOT / 'skills/apple-inspired-frontend', self.copy)

    def test_real_package(self):
        self.assertEqual(self.module.validate(self.copy), [])

    def test_missing_template_rejected(self):
        (self.copy / 'templates/CHANGE.md').unlink(missing_ok=True)
        self.assertTrue(any('missing: templates/CHANGE.md' in x for x in self.module.validate(self.copy)))

    def test_broken_relative_link_rejected(self):
        with (self.copy / 'SKILL.md').open('a') as f:
            f.write('\n[broken](references/absent.md)\n')
        self.assertTrue(any('broken link' in x for x in self.module.validate(self.copy)))

    def test_bad_frontmatter_rejected(self):
        p = self.copy / 'SKILL.md'
        p.write_text(p.read_text().replace('name: apple-inspired-frontend', 'name: Bad_Name'))
        self.assertTrue(any('frontmatter' in x for x in self.module.validate(self.copy)))

    def test_private_asset_rejected_even_untracked(self):
        (self.copy / 'private').mkdir()
        (self.copy / 'private/design.sketch').write_bytes(b'not an actual asset')
        self.assertTrue(any('forbidden asset' in x for x in self.module.validate(self.copy)))

    def test_private_path_rejected(self):
        p = self.copy / 'references/workflow.md'
        with p.open('a') as f:
            f.write('\n/home/example-user/private/design.json\n')
        self.assertTrue(any('private path' in x for x in self.module.validate(self.copy)))

    def test_escape_and_symlink_rejected(self):
        (self.copy / 'outside.md').symlink_to(Path(self.tmp.name))
        with (self.copy / 'SKILL.md').open('a') as f:
            f.write('\n[escape](../../outside.md)\n')
        errors = self.module.validate(self.copy)
        self.assertTrue(any('symlink' in x for x in errors))
        self.assertTrue(any('escapes package' in x for x in errors))

    def test_empty_template_rejected(self):
        (self.copy / 'templates/CHANGE.md').write_text('# CHANGE\n')
        self.assertTrue(any('template sections' in x for x in self.module.validate(self.copy)))

if __name__ == '__main__':
    unittest.main()
