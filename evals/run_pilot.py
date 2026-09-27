#!/usr/bin/env python3
"""Bounded local pilots. Raw records may contain machine paths: never publish local-runs.
No credentials/config are read or changed by this harness. CLI defaults select model.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('agent', choices=['claude', 'codex'])
    parser.add_argument('variant', choices=['none', 'current', 'v2'])
    parser.add_argument('--label', required=True)
    parser.add_argument('--seconds', type=int, default=150)
    parser.add_argument('--cliproxy', action='store_true', help='Isolated CODEX_HOME; existing endpoint/key via environment only')
    parser.add_argument('--skill-source', type=Path, help='Frozen current skill snapshot for comparable reruns')
    args = parser.parse_args()
    run = ROOT / 'evals/local-runs' / args.label
    if run.exists():
        raise SystemExit('Refusing to overwrite an existing run')
    project = run / 'project'
    shutil.copytree(ROOT / 'evals/fixture', project)
    subprocess.run(['git', 'init', '-q', str(project)], check=True)
    task = (ROOT / 'evals/tasks/small-change.md').read_text()
    if args.variant != 'none':
        directory = '.claude' if args.agent == 'claude' else '.agents'
        skill = project / directory / 'skills/apple-inspired-frontend'
        source = args.skill_source or ROOT / 'skills/apple-inspired-frontend'
        shutil.copytree(source, skill)
        task = f'먼저 {directory}/skills/apple-inspired-frontend/SKILL.md를 읽고 적용하세요.\n' + task
    task += '\n작업 디렉터리 내부의 파일만 읽고 수정하세요. 셸 명령이 허용되지 않으면 정적 코드 검토만 수행하고 그 한계를 보고하세요.'
    (run / 'prompt.txt').write_text(task)
    binary = shutil.which(args.agent)
    if not binary:
        raise SystemExit(f'{args.agent} unavailable')
    version = subprocess.run([binary, '--version'], capture_output=True, text=True, timeout=20)
    help_args = [binary, '--help'] if args.agent == 'claude' else [binary, 'exec', '--help']
    help_result = subprocess.run(help_args, capture_output=True, text=True, timeout=20)
    (run / 'help.txt').write_text(help_result.stdout + help_result.stderr)
    if args.agent == 'claude':
        command = [binary, '-p', '--output-format', 'json', '--no-session-persistence', '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}', '--no-chrome', '--tools', 'Read,Edit,Write', '--allowedTools', 'Read,Edit,Write', '--max-turns', '12', '--max-budget-usd', '2', task]
    else:
        command = [binary, 'exec', '--ephemeral', '--sandbox', 'workspace-write', '--json', '--color', 'never', task]
    env = os.environ.copy()
    if args.cliproxy:
        if args.agent != 'codex':
            raise SystemExit('--cliproxy is only for Codex')
        endpoint = env['CLIPROXY_BASE_URL']
        model = env['EVAL_CODEX_MODEL']
        if not env.get('CLIPROXY_API_KEY'):
            raise SystemExit('Missing secret environment reference')
        home = run / 'codex-home'
        home.mkdir()
        env['CODEX_HOME'] = str(home)
        command[2:2] = ['-c', 'model_provider="eval_proxy"', '-c', 'model=' + json.dumps(model), '-c', 'model_providers.eval_proxy.name="Existing Cliproxy (isolated eval)"', '-c', 'model_providers.eval_proxy.base_url=' + json.dumps(endpoint), '-c', 'model_providers.eval_proxy.env_key="CLIPROXY_API_KEY"', '-c', 'model_providers.eval_proxy.wire_api="responses"']
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in project.iterdir() if p.is_file()}
    start = time.monotonic()
    timed_out = False
    with (run / 'stdout.raw').open('w') as out, (run / 'stderr.raw').open('w') as err:
        proc = subprocess.Popen(command, cwd=project, env=env, stdin=subprocess.DEVNULL, stdout=out, stderr=err, start_new_session=True)
        try:
            code = proc.wait(timeout=args.seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                code = proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                code = proc.wait()
    record = dict(agent=args.agent, variant=args.variant, version=version.stdout.strip(), started_utc=started, elapsed_seconds=round(time.monotonic()-start, 3), timeout_seconds=args.seconds, timed_out=timed_out, exit_code=code, command=command, model=(env['EVAL_CODEX_MODEL'] + ' via isolated existing Cliproxy; /models verified by caller') if args.cliproxy else 'CLI configured default; see raw model usage/header when available', tools=('workspace-write sandbox; isolated CODEX_HOME, no configured MCP; browser/network forbidden by prompt') if args.cliproxy else ('Read/Edit/Write only, no MCP/browser' if args.agent == 'claude' else 'workspace-write sandbox; configured MCP may be discovered; prompt forbids network and browser'), before=before)
    (run / 'record.json').write_text(json.dumps(record, ensure_ascii=False, indent=2))
    print(json.dumps({k:v for k,v in record.items() if k not in ['command','before']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
