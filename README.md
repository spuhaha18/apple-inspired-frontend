# Apple-inspired Frontend

**Apple의 디자인 원칙을 프로젝트별 프론트엔드 명세로 연결하는 한국어 AI 에이전트 스킬.**

명료한 정보 위계, 일관된 조작, 읽기 쉬운 콘텐츠, 반응형과 접근성을 중심으로 `DESIGN.md`를 작성하고 구현 결과를 검토합니다. Apple처럼 보이는 유리 효과를 무조건 추가하거나 모든 제품을 같은 모양으로 만드는 스킬이 아닙니다.

> Apple과 무관한 독립 커뮤니티 프로젝트입니다. Apple 공식 UI 키트·컴포넌트 라이브러리·SwiftUI 또는 React 패키지가 아닙니다.

## 무엇을 제공하나요?

- **SKILL.md:** 요구사항 확인 → 참고자료 선택 → 디자인 명세 → 구현 → 검증 절차
- **DESIGN.md 템플릿:** 화면 구조·와이어프레임·토큰·상태·반응형·접근성·아이콘·근거 기록
- **웹 적용 가이드:** Apple native 원칙과 웹 프로젝트의 자체 결정 구분
- **UI 키트·SF Symbols 활용 가이드:** 플랫폼/자료 선택, 상태 피드백과 아이콘 기준
- **로컬 자료 확인 가이드:** 사용자가 보유한 Sketch 파일을 활용할 때의 출처·구조·시각 검증 구분
- **검토 체크리스트 및 공식 출처 링크**

### 포함하지 않는 것

Apple 문서 원문/영상 전사, Sketch/Figma 원본, Sketch 추출 JSON, 폰트, SF Symbols 기호, 스크린샷, 미리보기는 포함하지 않습니다. 내부 분석용 자료 전체를 공개하는 저장소가 아니라 **자체 작성한 지침·템플릿과 링크만 배포하는 공개판**입니다. 웹 조회나 UI 키트 접근이 차단되면 확인하지 못한 내용을 추측하지 않습니다.

## 빠른 시작

```bash
git clone https://github.com/spuhaha18/apple-inspired-frontend.git
cd apple-inspired-frontend
```

아래 에이전트별 목적지에 `skills/apple-inspired-frontend` **폴더 전체**를 복사합니다. `SKILL.md`만 복사하면 상대 경로로 연결된 참고자료를 읽지 못합니다. 동일 이름의 스킬이 이미 있다면 먼저 백업·비교하고 덮어쓰지 마세요.

### Claude Code

사용자 공통 경로: `~/.claude/skills/apple-inspired-frontend/`

```bash
mkdir -p ~/.claude/skills
# 대상 폴더가 없을 때만 실행
cp -R skills/apple-inspired-frontend ~/.claude/skills/
```

프로젝트 한정 설치는 `<project>/.claude/skills/apple-inspired-frontend/`를 사용합니다. 새 세션에서 다음과 같이 명시적으로 호출합니다.

```text
/apple-inspired-frontend
이 프로젝트의 요구사항과 기존 코드를 확인하고 DESIGN.md를 구체화해줘.
화면 구조·토큰·상태·반응형·접근성을 정의하고 아직 구현하지 말아줘.
```

### OpenAI Codex CLI / IDE

사용자 공통 경로: `~/.agents/skills/apple-inspired-frontend/`
프로젝트 한정 경로: `<project>/.agents/skills/apple-inspired-frontend/`

```bash
mkdir -p ~/.agents/skills
cp -R skills/apple-inspired-frontend ~/.agents/skills/
```

새 세션에서 `/skills`로 찾거나 다음과 같이 호출합니다.

```text
$apple-inspired-frontend
프로젝트를 분석해서 DESIGN.md를 작성해줘. 승인 전에는 구현하지 마.
```

### OpenCode

사용자 공통 경로: `~/.config/opencode/skills/apple-inspired-frontend/`
프로젝트 한정 경로: `<project>/.opencode/skills/apple-inspired-frontend/`

```bash
mkdir -p ~/.config/opencode/skills
cp -R skills/apple-inspired-frontend ~/.config/opencode/skills/
```

```text
apple-inspired-frontend 스킬을 로드하고 프로젝트의 DESIGN.md를 작성해줘.
```

OpenCode는 Claude/agents 호환 경로도 지원합니다. 이미 해당 경로에 설치했다면 중복 설치하지 마세요. 스킬은 native skill 도구로 읽으며 Claude Code의 슬래시 호출과 동일하다고 가정하지 않습니다.

### Hermes Agent

활성 프로필의 `skills/apple-inspired-frontend/`에 복사합니다. 기본 프로필 예시:

```bash
mkdir -p ~/.hermes/skills
cp -R skills/apple-inspired-frontend ~/.hermes/skills/
```

새 세션에서 “apple-inspired-frontend 스킬을 읽고 이 프로젝트의 디자인 명세를 작성해줘”라고 요청합니다. 프로필별 디렉터리를 사용하는 환경에서는 기본 경로를 다른 프로필의 경로와 혼동하지 마세요.

### OpenClaw

가장 명시적인 프로젝트 설치 위치는 해당 에이전트의 `<workspace>/skills/apple-inspired-frontend/`입니다. 실제 workspace 안에서 다음과 같이 복사합니다.

```bash
# 저장소에서 실행. 경로를 실제 workspace로 바꿀 것
mkdir -p /your/workspace/skills
cp -R skills/apple-inspired-frontend /your/workspace/skills/
```

새 세션에서 “apple-inspired-frontend 스킬로 DESIGN.md를 작성해줘”라고 요청합니다. 여러 에이전트/프로필에서 쓴다면 각 workspace와 스킬 허용 정책을 확인하세요.

### 그 밖의 에이전트 / Windows

Agent Skills 표준을 지원하는 도구는 해당 제품의 스킬 폴더에 전체 폴더를 복사하세요. 지원하지 않는 도구에는 `SKILL.md`와 연결된 참고문서를 명시적으로 읽도록 요청할 수 있지만 자동 인식은 보장하지 않습니다.
위 명령은 Linux/macOS/WSL 셸 기준입니다. Windows 네이티브는 탐색기로 같은 폴더 구조를 복사하면 됩니다. 홈 경로는 **에이전트를 실행하는 OS와 사용자 계정** 기준입니다. Windows 홈과 WSL 홈은 다릅니다.

## 프로젝트의 DESIGN.md 만들기

템플릿은 `skills/apple-inspired-frontend/templates/DESIGN.md`에 있습니다. 완성된 프로젝트 명세가 아니므로 대괄호 항목을 실제 결정으로 채워야 합니다.

```bash
# 기존 DESIGN.md가 없는 프로젝트에서만 실행
cp skills/apple-inspired-frontend/templates/DESIGN.md /your/project/DESIGN.md
```

1. 프로젝트 요구사항·기존 스택을 분석합니다.
2. 스킬로 DESIGN.md를 작성하고 시각 방향을 검토·승인합니다.
3. 승인된 명세로 구현합니다.
4. 브라우저·키보드·실제 화면·접근성·오류 상태를 검증합니다.

구현 요청 예시:

```text
apple-inspired-frontend 스킬과 승인된 DESIGN.md를 기준으로 구현해줘.
기존 컴포넌트 라이브러리를 유지하고 필요한 참고자료만 읽어줘.
구현 후 review-checklist.md에 따라 실제 검증 결과와 미검증 항목을 구분해줘.
```

### 프로젝트의 CLAUDE.md / AGENTS.md에 추가할 내용

기존 파일을 덮어쓰지 말고 해당 에이전트가 읽는 지침 파일에 병합합니다.

```markdown
## Frontend design
- 프론트엔드 설계·수정 시 apple-inspired-frontend 스킬을 읽는다.
- 구현 전에 프로젝트 루트 DESIGN.md를 읽는다.
- 승인된 프로젝트 명세와 기존 디자인 시스템을 우선한다.
- 명세 변경이 필요하면 먼저 설명하고 합의한다.
- Apple native 수치·자산을 웹에 그대로 적용하지 않는다.
- 실제 수행한 디자인·동작 검증과 미검증 사항을 구분해 보고한다.
```

## 사용 예: 업무용 웹

문서 검색·검토·승인 화면이라면 사이드바 → 제목/주 행동 → 검색/필터 → 목록/표 → 페이지 처리 구조부터 검토합니다. 콘텐츠는 읽기 쉬운 불투명 표면을 기본으로 하며, 강조 효과보다 저장/제출/승인 상태와 오류 복구를 명확히 합니다. 이는 프로젝트 적용 예시이지 Apple의 고정 레이아웃 규정이 아닙니다.

## 구조

```text
skills/apple-inspired-frontend/
├── SKILL.md
├── templates/DESIGN.md
└── references/
    ├── sources.md
    ├── web-adaptation.md
    ├── ui-kits-and-symbols.md
    ├── local-assets.md
    └── review-checklist.md
```

## 설치 확인과 한계

- 설치 폴더 바로 아래 `SKILL.md`가 있는지 확인합니다.
- 동일 이름의 중복 설치와 에이전트의 skill 차단 설정을 확인합니다.
- 새 세션에서 스킬을 명시적으로 호출하고 참고문서/템플릿 경로를 찾게 합니다.
- 이 공개판의 구조·상대 링크·금지 자산 포함 여부는 검증하지만, 위 모든 에이전트에서 실구동 테스트를 완료했다는 의미는 아닙니다. 설치 위치/호출법은 아래 공식 문서를 기준으로 정리했습니다.
- 스킬은 모델의 작업 지침이며 결과 품질이나 WCAG·GxP 적합성을 보장하지 않습니다.
- 복사 설치는 자동 동기화되지 않습니다. 업데이트 시 저장소 변경과 로컬 수정본을 비교해 반영하세요.

## 공식 문서

- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Codex skills](https://developers.openai.com/codex/skills/)
- [OpenCode skills](https://opencode.ai/docs/skills/)
- [Hermes documentation](https://hermes-agent.nousresearch.com/docs)
- [OpenClaw skills](https://docs.openclaw.ai/tools/skills)
- [Apple 출처 목록](skills/apple-inspired-frontend/references/sources.md)

## 저작권·이용 범위

본 저장소의 자체 작성 스킬·가이드·템플릿은 [LICENSE](LICENSE)를 참고하세요. Apple 및 다른 권리자의 문서·상표·폰트·아이콘·디자인 파일에는 해당 권리자의 조건이 적용됩니다. 링크 제공이나 로컬 파일 분석이 해당 자산의 재배포 허가를 뜻하지 않습니다. 자세한 범위는 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)에 명시합니다.
