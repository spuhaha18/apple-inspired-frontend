# 에이전트별 설치와 사용

공통 원본은 [SKILL.md](../skills/apple-inspired-frontend/SKILL.md)다. `skills/apple-inspired-frontend` 폴더 전체를 복사한다. 같은 이름의 설치본이 있으면 비교·백업하고 승인받아 교체한다. 이 문서는 자동 설치나 전역 설정 변경을 수행하지 않는다.

## Claude Code
- 프로젝트: `.claude/skills/apple-inspired-frontend/`
- 사용자: `~/.claude/skills/apple-inspired-frontend/`
- 호출: `/apple-inspired-frontend` 뒤에 작업 요청을 적는다. 인식되지 않으면 실제 SKILL.md 경로를 명시해 읽도록 한다.
- [공식 문서](https://code.claude.com/docs/en/skills)
- 확인 수준: Claude Code 2.1.283에서 파일 경로를 명시한 Read/Edit/Write 파일럿 적용 성공. native 자동 발견·슬래시 호출·실제 화면 검증은 미실행.

## Codex CLI / IDE
- 프로젝트: `.agents/skills/apple-inspired-frontend/`
- 사용자: `~/.agents/skills/apple-inspired-frontend/`
- 호출: `$apple-inspired-frontend`와 작업 요청. 인식되지 않으면 실제 SKILL.md 경로를 명시한다.
- [공식 문서](https://developers.openai.com/codex/skills/)
- 확인 수준: CLI 0.135.0에서 기존 프록시를 통한 실제 모델 응답 확인. 샌드박스 권한 오류로 파일 읽기·적용은 차단됨. native discovery·IDE·구현 품질은 미검증. 연결 성공은 적용 성공이 아니다.

## OpenCode
- 프로젝트: `.opencode/skills/apple-inspired-frontend/`
- 사용자: `~/.config/opencode/skills/apple-inspired-frontend/`
- 요청: “apple-inspired-frontend 스킬을 로드하고 기존 명세를 읽어 작업해줘.”
- [공식 문서](https://opencode.ai/docs/skills/)
- 호환 경로에 이미 설치했다면 중복 설치를 피한다. Claude의 슬래시 호출과 같다고 가정하지 않는다.
- 확인 수준: 문서 기반 안내, v2 실구동 적용 미검증.

## Hermes Agent
- 활성 프로필의 `skills/apple-inspired-frontend/`. 기본 프로필 예시는 `~/.hermes/skills/apple-inspired-frontend/`다.
- 요청: “apple-inspired-frontend 스킬을 읽고 이 프로젝트를 검토해줘.”
- [공식 문서](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- 확인 수준: 문서 기반 안내. 다른 프로필 자동 설치나 v2 설치 완료를 의미하지 않는다.

## OpenClaw
- 해당 에이전트 workspace의 `skills/apple-inspired-frontend/`에 설치한다.
- 요청: “apple-inspired-frontend 스킬로 프로젝트의 디자인 명세를 작성해줘.”
- [공식 문서](https://docs.openclaw.ai/tools/skills)
- workspace와 허용 정책을 확인한다. 다른 에이전트 workspace까지 변경하지 않는다.
- 확인 수준: 문서 기반 안내, v2 실구동 적용 미검증.

## 그 밖의 에이전트 / Windows
Agent Skills 지원 도구는 제품 공식 설치 경로에 전체 폴더를 복사한다. 미지원 도구도 SKILL.md와 연결된 문서를 명시적으로 읽을 수 있다면 활용 가능하지만 자동 인식·동일 동작은 보장하지 않는다. Windows 네이티브와 WSL의 홈은 다르며 경로는 에이전트를 실행하는 OS와 사용자 기준이다.

## 공통 실행·인계
1. 프로젝트 지침과 기존 DESIGN.md를 읽는다.
2. 신규/기존 개선/작은 변경/리뷰 모드를 선택한다. 작은 수정에 전체 명세 재작성을 강제하지 않는다.
3. 승인된 범위와 기존 브랜드·스택을 유지한다.
4. 변경 파일·결정 이유·실제 검증·미검증을 기록한다.
5. 다른 에이전트는 같은 명세와 변경 기록으로 이어받는다.

브라우저가 없으면 시각 검증을 미검증으로 남긴다. 샌드박스 오류를 이유로 보안을 임의 해제하지 않는다. 실제 시험 범위는 [평가 결과](../evals/results.md)를 따른다. 설치 시 공식 문서에서 최신 경로·호출법을 재확인한다.
