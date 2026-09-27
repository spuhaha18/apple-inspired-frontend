# Executable web skill v2 Implementation Plan

> **For agentic workers:** Use executing-plans task-by-task. This branch is already isolated; user approved local implementation. Parent owns final review.

**Goal:** 한국어 실행 계약과 오프라인 패키지, 실제 CLI 파일럿, 재현 가능한 구조 검사를 제공한다.
**Architecture:** 공통 SKILL은 모드 라우터다. workflow/판단/패턴/프로필이 판단을 소유하고 템플릿은 산출물 구조를 소유한다. evals는 배포 스킬 밖에 둔다.
**Tech Stack:** Markdown, Python 3 표준 라이브러리, 고정 HTML/CSS/JS, 기존 Claude/Codex CLI.

## Global Constraints
- `skills/apple-inspired-frontend/` 유지. Apple 자산과 개인 경로/비밀정보를 공개 패키지에 넣지 않는다.
- 전역 설정/설치/자격증명 변경, push, publish 없음. Git identity를 만들지 않으며 commit은 보류한다.
- 모드는 신규 설계/기존 개선/작은 변경/리뷰. DOM 검사와 시각 검증을 분리한다.
- 라이선스와 기존 자산 관련 안전 문서를 보존한다. 예산 제한 파일럿은 반복 비교 평가를 대체하지 않는다.

## 실행 상태 (부모 검토 인계)
- Task 1 완료: 수정 전 Claude none/current 행동 기록, Codex 기본 인증 실패 기록, baseline.md에 실제 관찰. 비례성 실패 가설은 지지되지 않아 영속 CHANGE/측정 근거 차이를 대상으로 삼음.
- Task 2 완료: 구조 RED → 구현 → 8개 테스트 GREEN, 음성 변이와 실제 현행 패키지 누락 확인.
- Task 3 완료: 네 모드/조건부 규칙/네 패턴/프로필/도구 역량/세 템플릿/세 완성 예시. 테스트된 v2 복사본과 현재 패키지 바이트 일치 확인.
- Task 4 부분 완료: Claude 실제 적용, Codex 기존 프록시 실제 응답(파일 적용은 bwrap 차단), 네 과제/rubric/evidence/results/README. `docs/agents.md`는 보호된 파일 쓰기 거부로 미작성; 승인 필요. 자동 발견·전체 비교·시각 검증 미완료를 명시.
- 최종 확인: package 검사/8 tests PASS, 모든 공개 Markdown 상대 파일 링크 유효, git diff --check PASS, LICENSE/THIRD_PARTY_NOTICES 변경 없음.
- 커밋 보류: Git identity 없음. push/publish/global install 없음. 부모 작업을 종료하지 않음.

## Task 1 — baseline evidence before skill edits
Files: `evals/fixture/*`, `evals/tasks/*`, `evals/run_pilot.py`, ignored `evals/local-runs/*`.
- [ ] 고정 브랜드, 검색, 저장 실패 fixture와 작은 변경 프롬프트를 작성한다.
- [ ] CLI version/help를 저장한다. 모델 플래그 없이 현재 default 사용, tool/시간 한도를 기록한다.
- [ ] 새 디렉터리에서 무지침과 현재 SKILL 입력으로 같은 작은 변경 판단을 실행한다.
- [ ] raw stdout/stderr/exit/command/time을 저장하고 실제 결과를 읽는다. 이미 정직한 검증 보고라면 실패로 꾸미지 않고 전체 DESIGN gate 비례성 차이를 확인한다.

## Task 2 — test-first structure contract
Files: `tests/test_package.py`, `scripts/check_package.py`.
- [ ] required files/4 modes/templates/relative links/frontmatter/private assets 계약 테스트를 먼저 작성한다.
- [ ] `python3 -m unittest discover -s tests -v`를 실행하고 아직 없는 checker 실패를 기록한다.
- [ ] `validate(root: Path) -> list[str]` 인터페이스의 stdlib checker를 구현한다. 누락 파일, 깨진 링크, 잘못된 메타데이터, 자산/개인경로에 대해 오류를 반환한다.
- [ ] 변이 fixture로 각 실패 경로를 실행한다. 실제 패키지 검사는 v2 작성 전 실패해야 한다.

## Task 3 — offline execution guidance
Files: SKILL, workflow, decision-rules, project-profiles, tool-capabilities, four patterns, review-checklist, templates DESIGN/CHANGE/REVIEW, `examples/*`.
- [ ] 네 모드의 조건→행동→산출물→완료 조건을 작성한다. 작은 변경은 CHANGE만, 리뷰는 무편집이다.
- [ ] 패턴마다 사용 조건/선택/예외/구성/상태/작은 화면/키보드/좋고 나쁜 예/검증/출처 구분을 작성한다.
- [ ] 전체 템플릿을 실무 결정 슬롯으로 고치고 완성 예시 3개를 작성한다.
- [ ] `python3 scripts/check_package.py`와 unit tests를 실행해 green 확인한다.

## Task 4 — actual application pilots and installation docs
Files: `docs/agents.md`, README, evals tasks/rubric/results, runner.
- [ ] 공식 제품 문서를 조회하여 경로·호출법을 확인하고 조회 출처/확인 수준을 기록한다.
- [ ] 깨끗한 project-local skill copies로 Claude/Codex 각각 제한된 실제 변경 파일럿을 실행한다.
- [ ] 실패는 stderr와 exit를 남기고 최대 1회만 재시도한다. 브라우저 검증 성공을 추정하지 않는다.
- [ ] 실제 편집과 fixture check를 확인한다. no-guidance/current/v2 차이는 같은 에이전트 안에서만 해석한다.
- [ ] 네 과제와 0/1/2 rubric, raw 기록 형식, 실행 제한과 후속 리뷰 공백을 작성한다.
- [ ] 최종 구조 검사, unit tests, `git diff --check`, 라이선스 diff, package 파일 목록을 확인한다. 결과는 부모에게 인계하며 부모 작업은 닫지 않는다.
