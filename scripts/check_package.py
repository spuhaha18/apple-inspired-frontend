#!/usr/bin/env python3
"""Offline stdlib structural guard, not a UI/security/license certification.
Supported Markdown links: inline links/images and reference definitions. Fenced
code is excluded; anchors are not resolved. All package files must be Markdown.
"""
from pathlib import Path
import argparse
import re
from urllib.parse import unquote, urlsplit

REQUIRED = ['SKILL.md', *('references/' + name + '.md' for name in ['workflow', 'decision-rules', 'project-profiles', 'tool-capabilities', 'review-checklist', 'sources', 'web-adaptation', 'ui-kits-and-symbols', 'local-assets']), *('references/patterns/' + name + '.md' for name in ['navigation', 'data-display', 'forms-feedback', 'visual-system']), *('templates/' + name + '.md' for name in ['DESIGN', 'CHANGE', 'REVIEW'])]
SECTIONS = {
    'DESIGN': ['진단', '방향', '구조', '토큰', '상태', '반응형', '검증', '승인'],
    'CHANGE': ['범위', '재사용', '상태', '검증', '인계'],
    'REVIEW': ['범위', '증거', '발견', '미검증', '후속'],
}

def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append('missing: ' + name)
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f'symlink: {relative}')
            continue
        if any(part in {'private', 'corpus', 'local-assets', '.git'} for part in relative.parts) or (path.is_file() and path.suffix != '.md'):
            errors.append(f'forbidden asset: {relative}')
        if not path.is_file() or path.suffix != '.md':
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append(f'non-UTF8 text: {relative}')
            continue
        if re.search(r'(?:/home/|/Users/|[A-Z]:[\\/]Users[\\/])[^\s`]+', text):
            errors.append(f'private path: {relative}')
        if re.search(r'(?:sk-[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY-----)', text):
            errors.append(f'possible secret: {relative}')
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        targets = re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)', prose)
        targets += re.findall(r'^\s*\[[^\]]+\]:\s*(\S+)', prose, flags=re.M)
        for target in targets:
            target = target.strip('<>')
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resolved = (path.parent / unquote(parts.path)).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f'link escapes package: {relative}: {target}')
            elif not resolved.exists():
                errors.append(f'broken link: {relative}: {target}')
    skill = root / 'SKILL.md'
    if skill.is_file():
        text = skill.read_text()
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        values = dict(re.findall(r'^(name|description):\s*(.+)$', match[1], re.M)) if match else {}
        if values.get('name') != root.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', values.get('name', '')) or not values.get('description', '').startswith('Use when') or len(values.get('description', '')) > 1024:
            errors.append('frontmatter: required name/description contract failed')
        for mode in ['신규 설계', '기존 개선', '작은 변경', '리뷰']:
            if mode not in text:
                errors.append('missing mode: ' + mode)
    for name, sections in SECTIONS.items():
        path = root / 'templates' / (name + '.md')
        if path.exists():
            headings = '\n'.join(re.findall(r'^## .*$', path.read_text(), re.M))
            for section in sections:
                if section not in headings:
                    errors.append(f'template sections: {name}: {section}')
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', type=Path, default=Path(__file__).resolve().parents[1] / 'skills/apple-inspired-frontend')
    args = parser.parse_args()
    errors = validate(args.path)
    print('\n'.join(errors) if errors else 'PASS: package structure, metadata, relative targets, templates, asset boundaries')
    raise SystemExit(bool(errors))

if __name__ == '__main__':
    main()
