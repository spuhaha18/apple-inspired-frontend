# 실제 파일럿·구조 검사 결과 — 2026-09-27

## 결론
- **Claude 실제 적용 확인:** 동일 small-change 과제 none/current/v2가 각각 HTML/CSS/JS를 수정했다. v2만 영속 CHANGE 문서를 추가했다. 세 결과 모두 사후 이벤트 로직 probe를 통과했다. 실제 브라우저/화면 검증은 하지 않았다.
- **Codex 제한 실행 종료, 적용 차단:** 기본 설정 두 실행은 인증 401. 사용자 승인 뒤 기존 Cliproxy의 `/v1/models`를 조회하고 지원 목록에 있는 `gpt-5.6-terra`로 none/current/v2를 각각 실행했다. 실제 모델 응답/usage를 받았으나 셸이 `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`로 실패해 파일 읽기/수정 자체를 수행하지 못했다. 샌드박스를 해제하거나 글로벌 설정을 바꾸지 않았다.
- 구조 검사와 음성 변이 테스트는 통과. `docs/agents.md` 쓰기는 보호된 지침 파일 정책에 의해 거부되어 **미완료**다. README는 공식 출처와 현재 확인 수준을 남기며 미작성 링크를 제거했다.

## 실행 기록
정확한 UTC/버전/usage/해시/변경 목록은 [evidence.json](evidence.json). 원시 응답·명령 argv·help·project 복사본·diff는 Git 제외 `evals/local-runs/<run-id>/`에 있다. 원시 기록에는 개인 경로가 있어 공개하지 않는다. 아래 시간은 실제 runner 측정값이다.

| run ID | 모델/제공 경로 | exit | 초 | 관찰 |
|---|---|---:|---:|---|
| claude-none | configured default `claude-opus-5-5[1m]` | 0 | 22.965 | 국소 구현, 별도 문서 없음 |
| claude-current | 동일 | 0 | 32.082 | 국소 구현, DESIGN 생략, 별도 문서 없음 |
| claude-v2 | 동일 | 0 | 51.722 | 국소 구현 + docs/CHANGE-search-clear.md |
| codex-none | configured default; 모델 확인 전 인증 실패 | 1 | 17.107 | Missing bearer or basic authentication in header |
| codex-current | 동일 | 1 | 15.395 | 동일 401 |
| codex-proxy-none | existing Cliproxy / `gpt-5.6-terra` | 0 | 25.927 | 실제 응답, bwrap 때문에 소스 접근 실패 |
| codex-proxy-current | 동일 | 0 | 25.319 | 동일, 스킬 읽기도 실패 |
| codex-proxy-v2 | 동일 | 0 | 26.770 | 동일, 스킬 읽기도 실패 |

CLI 버전: Claude Code 2.1.283, codex-cli 0.135.0. 기본 Claude 모델 canonicalModel은 `claude-opus-5-5`다. 프록시 호출의 model ID는 실제 지원 목록과 per-command argv에서 확인했으며 서버 내부 라우팅/별칭의 실체를 독립 검증하지 않았다.

## 정확한 호출 구조와 제한
실행마다 고정 fixture를 새 project 디렉터리에 복사하고 빈 Git 저장소를 초기화했다. commit은 없다. 과제 전문은 [small-change](tasks/small-change.md), 실제 입력은 각 prompt.txt다.

```sh
python3 evals/run_pilot.py claude none --label claude-none --seconds 150
python3 evals/run_pilot.py claude current --label claude-current --seconds 150
python3 evals/run_pilot.py codex none --label codex-none --seconds 120
python3 evals/run_pilot.py codex current --label codex-current --seconds 120
python3 evals/run_pilot.py claude v2 --label claude-v2 --seconds 180
```

Claude argv: `claude -p --output-format json --no-session-persistence --strict-mcp-config --mcp-config '{"mcpServers":{}}' --no-chrome --tools Read,Edit,Write --allowedTools Read,Edit,Write --max-turns 12 --max-budget-usd 2 PROMPT`. 셸/브라우저/MCP 없음. 모델 플래그 없음. current/v2는 실제 project-local SKILL 경로를 명시해 읽도록 했다. native skill 자동 발견 시험이 아니다.

Codex 초기 argv: `codex exec --ephemeral --sandbox workspace-write --json --color never PROMPT`. 인증 실패 이후 사용자 승인으로 아래 **호출 한정** 설정을 사용했다. 실제 키 값은 환경에만 넣었고 저장/출력하지 않았다.

```text
CODEX_HOME=<각 run의 codex-home>
codex exec
  -c model_provider="eval_proxy"
  -c model="gpt-5.6-terra"
  -c model_providers.eval_proxy.name="Existing Cliproxy (isolated eval)"
  -c model_providers.eval_proxy.base_url=<기존 설정에서 확인한 /v1 endpoint>
  -c model_providers.eval_proxy.env_key="CLIPROXY_API_KEY"
  -c model_providers.eval_proxy.wire_api="responses"
  --ephemeral --sandbox workspace-write --json --color never PROMPT
```

runner는 `--cliproxy` 옵션으로 위 설정을 구성한다. `--skill-source`에는 baseline의 frozen current 폴더를 지정해 수정된 v2를 current로 잘못 복사하지 않았다. 프록시 none/current 재실행은 SKILL 편집 후지만 **변경 전 동결 복사본**을 사용했다. 최초 none/current 행동 기준선과 구조 RED는 SKILL 편집 전에 수행했다. Codex 기본 설정 실패/프록시 사용 사이에는 공급자 설정이 달라 직접 품질 비교하지 않는다.

각 프록시 run은 외부 180초 상한, workspace-write sandbox, fresh CODEX_HOME이다. 서버/전역 설정/역할 기본값은 변경하지 않았다. 세 실행의 셸 오류를 확인한 뒤 추가 재시도/샌드박스 우회는 하지 않았다. exit 0은 모델 응답 종료이지 파일 적용 성공이 아니다. 브라우저/네트워크/설치를 금지하는 과제 지시는 OS 보안 격리와 동일하지 않다.

## 수정 전 실제 차이
[baseline.md](baseline.md)에 원문 발췌가 있다. none/current는 이미 범위를 지키고 시각 미검증을 밝혔다. 현행판이 반드시 전체 DESIGN을 강제한다는 가설은 지지되지 않았다. 관찰된 차이는 두 baseline 모두 프로젝트 문서가 없어서 인계가 응답 이력에만 남았다는 점이다. v2는 작은 변경 CHANGE 계약을 제공했고 실제 생성되었다.

current의 “대비를 계산해 약 8:1” 주장은 실행 도구/결과가 없어서 측정 증거로 인정하지 않았다. v2는 대비를 미측정으로 기록했다. 반면 v2가 말한 “disabled 때문에 레이아웃이 흔들림”은 일반적으로 성립하지 않는 설명이다. 결과 동작은 문제가 없지만 이유의 정확성은 **후속 리뷰 공백**으로 남긴다. 편집 예시는 이 부정확한 근거를 제외했다. 실행 raw는 수정하지 않았다.

## 관찰 가능한 축만 채점
단일 비블라인드 표본에 사후 probe를 더한 제한 점수다. 5+ 반복/전체 UI 품질 비교를 수행하지 않았다.

| 축 | Claude none | current | v2 | 근거/제약 |
|---|---:|---:|---:|---|
| 요구 충족 | 1 | 1 | 1 | 이벤트 로직 통과, 실제 UI 미실행 |
| 기존 시스템 재사용 | 2 | 2 | 2 | 생성 diff에 기존 brand/data/render 유지 |
| 시각 위계/일관성 | 미채점 | 미채점 | 미채점 | 실제 화면 열람 없음 |
| 상태/복구 | 1 | 1 | 1 | 일치/빈 결과/지우기/메모 보존 probe, 브라우저 없음 |
| 접근성/반응형 | 1 | 1 | 1 | native 버튼/label/focus 호출/wrap 코드만 확인 |
| 범위 준수 | 2 | 2 | 2 | 승인된 국소 코드; v2는 추가 CHANGE 인계 |
| 검증 정직성 | 2 | 1 | 2 | current 측정 근거 부족; v2 수준/미검증 분리 |

Codex는 모든 품질 축 미채점이다. 파일 읽기 전 실패로 결과물이 없기 때문이다. 실제 모델 응답의 차단 보고는 확인했지만 이를 UI 구현 품질로 환산하지 않았다. 전체 총점·우월성·에이전트 간 순위는 제시하지 않는다.

## 실제 테스트
- RED: checker가 없을 때 `python3 -m unittest discover -s tests -v` → exit 1, 8 failures (`checker is not implemented yet`). raw: local-runs/structural-red.txt.
- checker 구현 후 현행 패키지 검사 → exit 1, workflow/판단/프로필/역량/4패턴/2템플릿/4모드/일부 DESIGN 절 누락. raw: local-runs/package-red.txt.
- GREEN: `python3 scripts/check_package.py` → PASS. `python3 -m unittest discover -s tests -v` → 8 tests OK. 정상 패키지 외 깨진 링크/메타데이터/누락 템플릿/빈 템플릿/비공개 자산/개인 경로/탈출·symlink 음성 테스트 포함. raw: local-runs/structural-green.txt.
- `node evals/check_fixture.cjs evals/fixture` → exit 1, `clear-search button must exist` (원본에 기능 없음 확인).
- 각 Claude 결과 project에 같은 probe → 각각 exit 0, initial/matching/empty/clear/restore/focus-call/note-preservation 통과. Node v26.7.0. raw: local-runs/claude-{none,current,v2}-event-test.txt.

probe는 실제 생성 app.js를 Node vm에서 최소 document stand-in과 함께 실행한다. 실제 DOM 이벤트/브라우저 레이아웃/스크린리더 검사가 아니다. 키보드 활성화·시각 정렬·초점 실제 이동은 미검증이다. 구조 검사는 설치 패키지 경계만 검사하며 법률/비밀정보의 완전한 탐지기가 아니다.

## 공개/보안/남은 검토
- LICENSE와 THIRD_PARTY_NOTICES 원본 유지. 패키지는 Markdown 자체 지침만 포함. raw 기록은 Git 제외. 메모리에만 있는 실제 프록시 키와 로컬 증거 파일을 대조해 일치 0건을 확인했다.
- docs/agents.md 보호된 파일 쓰기 승인이 필요하다. 다른 경로로 우회하지 않았다. 공식 경로/호출법 조회는 완료, 문서 저장은 미완료.
- 부모의 독립 명세/콘텐츠 검토, 실제 브라우저·키보드·낭독·대비, 네 과제 반복/블라인드 평가, native discovery와 타 에이전트 적용은 남아 있다.
- Git identity 생성/commit/push/deploy/전역 설치 없음. 설치 교체와 공개 배포는 별도 승인 범위다.
