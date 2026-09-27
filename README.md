# Apple-inspired Frontend v2

**기존 브랜드를 유지하며 웹 UI를 조사 → 판단 → 구현 → 검증하는 한국어 에이전트 스킬.**

Apple HIG의 명료한 위계·일관된 조작·가독성 원칙을 참고합니다. 유리 효과나 Apple 외관을 일괄 적용하는 프리셋이 아닙니다. 웹이 실행 대상이며 네이티브는 참고 범위입니다.

> Apple과 무관한 독립 커뮤니티 프로젝트입니다. Apple 공식 UI 키트·컴포넌트 라이브러리·SwiftUI/React 패키지가 아닙니다.

## 요청 크기에 맞는 네 모드
| 모드 | 실행 | 기록 |
|---|---|---|
| 신규 설계 | 진단 → 방향 승인 → 대표 화면 → 검증/수정 → 확장 | DESIGN |
| 기존 개선 | 문제 증거 → 영향 명세 → 필요한 방향 합의 → 구현/회귀 | DESIGN 영향 절 + 검증 |
| 작은 변경 | 관련 명세/코드 → 영향 기록 → 구현/회귀 | CHANGE; 전체 DESIGN 재작성 없음 |
| 리뷰 | 조사 → 근거/심각도/권고 | REVIEW; 요청 없는 코드 수정 없음 |

이미 승인된 범위는 반복 승인 없이 실행합니다. 브랜드·탐색·핵심 동작 변경과 범위 확장은 합의합니다. 브라우저가 없으면 가능한 코드 작업과 시각 검증 대기를 분리합니다.

## 빠른 시작
저장소의 `skills/apple-inspired-frontend/` **폴더 전체**를 대상 프로젝트의 스킬 위치에 복사합니다. 기존 같은 이름이 있으면 백업·비교하고 덮어쓰지 마세요. 프로젝트 한정 설치를 우선 권장합니다.

- Claude Code: `.claude/skills/apple-inspired-frontend/`, 새 세션 `/apple-inspired-frontend`
- Codex: `.agents/skills/apple-inspired-frontend/`, 새 세션 `$apple-inspired-frontend`
- 그 밖의 제품 설치 및 상세 호출법은 [docs/agents.md](docs/agents.md)를 확인하세요. 아래 공식 문서에서 최신 실행 환경별 경로를 재확인할 수 있습니다.

공식 문서 확인(2026-09-27): [Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://developers.openai.com/codex/skills/), [OpenCode](https://opencode.ai/docs/skills/), [Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/), [OpenClaw](https://docs.openclaw.ai/tools/skills).
실제 자동 발견/슬래시 호출은 미검증이며 파일럿은 파일 경로를 명시해 읽도록 요청했습니다. OpenCode/Hermes/OpenClaw는 공식 문서 확인만 수행했습니다. 복사 설치는 자동 동기화되지 않으며 같은 이름의 전역/프로젝트 중복과 실행 OS의 홈 경로를 확인해야 합니다.

```text
apple-inspired-frontend를 읽고 기존 브랜드를 유지해 검색 지우기 버튼을 추가해줘.
이 국소 변경은 승인했어. 관련 명세/코드를 읽고 작은 변경 기록을 남겨줘.
실제 수행한 검사와 브라우저가 없어 하지 못한 검사를 구분해줘.
```

신규 설계 요청은 “방향 명세부터 작성하고 승인 전 구현하지 마”로, 리뷰 요청은 “코드 변경 없이 근거·심각도·권고를 작성해줘”로 범위를 정할 수 있습니다. 특정 브라우저/MCP/패키지를 설치할 필요는 없습니다. 외부 조회 없이 핵심 판단과 템플릿을 사용할 수 있으며 최신 정책/자산 권한은 필요할 때 공식 출처로 확인합니다.

## 구성과 읽기 경로
- [공통 SKILL](skills/apple-inspired-frontend/SKILL.md): 모드와 실행/승인/인계 계약
- [workflow](skills/apple-inspired-frontend/references/workflow.md), [조건별 판단](skills/apple-inspired-frontend/references/decision-rules.md), [프로젝트 유형](skills/apple-inspired-frontend/references/project-profiles.md)
- [탐색](skills/apple-inspired-frontend/references/patterns/navigation.md), [데이터](skills/apple-inspired-frontend/references/patterns/data-display.md), [폼/피드백](skills/apple-inspired-frontend/references/patterns/forms-feedback.md), [시각 체계](skills/apple-inspired-frontend/references/patterns/visual-system.md)
- [도구 역량](skills/apple-inspired-frontend/references/tool-capabilities.md), [검증 체크리스트](skills/apple-inspired-frontend/references/review-checklist.md)
- [DESIGN](skills/apple-inspired-frontend/templates/DESIGN.md), [CHANGE](skills/apple-inspired-frontend/templates/CHANGE.md), [REVIEW](skills/apple-inspired-frontend/templates/REVIEW.md) 템플릿
- 저장소 전용 완성 예시: [설계](examples/DESIGN-worklist.md), [작은 변경](examples/CHANGE-search-clear.md), [리뷰](examples/REVIEW-fixture.md). 설치 필수 자료가 아니며 실제 검증 한계를 표시합니다.
- [웹 적용/자체 시작값](skills/apple-inspired-frontend/references/web-adaptation.md), [자산·아이콘](skills/apple-inspired-frontend/references/ui-kits-and-symbols.md), [로컬 자료](skills/apple-inspired-frontend/references/local-assets.md), [공식 출처](skills/apple-inspired-frontend/references/sources.md)

## 검증 결과와 한계
[평가 기록](evals/results.md)과 [재실행 안내](evals/README.md)를 제공합니다. 스킬 수정 전에 무지침/현행판 기준선을 실행했습니다. Claude v2는 실제 국소 코드 변경과 CHANGE를 생성했습니다. Codex는 승인된 기존 프록시로 실제 모델 응답을 받았으나 샌드박스 오류 때문에 파일 적용은 차단되었습니다. **양쪽 전체 적용 검증 완료 또는 UI 품질 우월성을 주장하지 않습니다.**

Python 표준 라이브러리만으로 오프라인 검사합니다:

```sh
python3 scripts/check_package.py
python3 -m unittest discover -s tests -v
```

검사는 패키지 상대 파일 링크, 메타데이터, 필수 문서/템플릿 절, 비공개 자산 경계와 실패 변이를 확인합니다. URL 최신성·Markdown anchor·디자인 품질·완전한 비밀 탐지/법률 검토는 보장하지 않습니다. 이벤트 로직 probe는 Node가 이미 있으면 실행할 수 있으며 브라우저/실제 DOM 검증은 아닙니다. 어떤 결과도 WCAG/GxP 인증을 뜻하지 않습니다.

## 공개 패키지 경계·저작권
Apple 문서 원문/영상 전사, Sketch/Figma/추출 JSON, 폰트, SF Symbols 기호, 공식 스크린샷/미리보기는 배포하지 않습니다. 자체 지침·템플릿·링크만 포함합니다. 저장소의 가상 fixture는 직접 작성한 예제이며 실제 업무 데이터가 아닙니다. 개인 경로가 포함될 수 있는 raw 파일럿 기록은 `evals/local-runs/`에 보관하고 Git에서 제외합니다.

자체 작성물은 [LICENSE](LICENSE)를 참고하세요. Apple 및 다른 권리자의 문서·상표·폰트·아이콘·디자인 파일은 별도 이용 조건을 따릅니다. 링크 제공이나 로컬 분석은 재배포 허가가 아닙니다. [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md)를 유지합니다.
