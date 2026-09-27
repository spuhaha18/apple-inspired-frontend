---
name: apple-inspired-frontend
description: Use when designing, implementing, improving, or reviewing web frontend UI, including small changes within an existing brand and project design specifications.
---

# Apple-inspired frontend — 실행 계약

Apple HIG를 설계 근거로 삼는 독립 커뮤니티 스킬이다. 기존 브랜드·사용자 요구·승인 명세가 우선이다. 같은 모양의 화면을 찍어내는 프리셋이나 Apple 공식 UI 라이브러리가 아니다. 웹을 실행 대상으로 하며 네이티브는 참고 범위다.

## 먼저 모드를 선택한다

| 시작 조건 | 모드와 행동 | 산출물 | 완료 조건 |
|---|---|---|---|
| 새 제품/화면의 방향과 구조를 정해야 한다 | **신규 설계**: 진단 → 방향 명세 → 승인 → 대표 화면 → 검토/수정 → 확장 | [DESIGN](templates/DESIGN.md), 검증 기록 | 승인 범위 구현, 대표 화면 검토, 남은 검증 명시 |
| 기존 흐름/위계에 근거 있는 문제가 있고 여러 요소가 영향을 받는다 | **기존 개선**: 현황과 문제 증거 → 변경안 → 방향 변경 합의 → 구현/회귀 | 기존 DESIGN의 영향 절 수정, 검증 기록 | 문제 재현과 수정 후 재검증, 범위 밖 유지 |
| 승인된 국소 기능/문구/스타일 변경이고 브랜드·탐색·핵심 동작은 유지한다 | **작은 변경**: 기존 명세와 관련 코드 → 영향 기록 → 구현/회귀 | [CHANGE](templates/CHANGE.md)를 프로젝트 관례 경로에 저장 | 요구 동작·범위 확인, 실행/미실행을 기록한 인계 파일 |
| 사용자가 평가/검토만 요청한다 | **리뷰**: 조사 → 근거 → 심각도/권고 | [REVIEW](templates/REVIEW.md) | 근거와 미검증 구분; 코드 변경 없음 |

작은 변경이면 전체 DESIGN을 새로 만들지 않고 CHANGE만 작성한다. 기존 DESIGN이 없으면 ‘없음’과 재사용한 코드/토큰을 기록한다. 파일 쓰기 권한이 없으면 같은 항목을 응답으로 인계한다. 이미 승인된 범위의 구현은 다시 승인받지 않는다. 브랜드·탐색·핵심 동작 변경 또는 범위 확장이 발견되면 변경 부분만 합의한다.

## 공통 실행 순서

1. **진단:** 프로젝트 지침, 의존성/실행 명령, 라우팅, 전역 스타일/토큰, 관련 컴포넌트/테스트를 읽는다. 코드에 있는 답은 직접 찾는다. 핵심 작업·환경·재사용·범위·미확인을 기록한다. [workflow](references/workflow.md)와 [도구 역량](references/tool-capabilities.md)을 따른다.
2. **판단:** [프로젝트 프로필](references/project-profiles.md)과 [조건별 규칙](references/decision-rules.md)에서 해당 분기만 선택한다. 확정되지 않은 고위험 결정만 질문한다.
3. **명세:** 모드별 문서에 주 행동, 위계, 토큰, 상태/복구, 반응형, 키보드를 결정한다. 적용 안 되는 상태에는 이유를 쓴다. 새 방향이면 구현 전에 합의한다.
4. **구현:** 기존 스택·공통 컴포넌트·토큰을 재사용하고 상태별 동작을 함께 만든다. 큰 작업이면 대표 화면을 검토한 뒤 확장한다. 예시 데이터에는 가상 표시를 둔다.
5. **검증/수정:** 기존 테스트와 영향 동작, 키보드·반응형·실제 화면을 [체크리스트](references/review-checklist.md)로 검증한다. 실패를 고치고 영향 항목을 다시 실행한다. 브라우저가 없으면 코드 검토/실행 결과와 시각 미검증을 분리한다.
6. **인계:** 변경 파일, 결정/승인 근거, 실제 명령·결과·증거 위치, 미검증과 다음 조치를 남긴다. 계산·측정은 도구/입력/결과를 기록하며 추정은 측정값으로 채점하지 않는다.

## 필요한 문서만 읽는다
- 경로·메뉴·탭 변경: [탐색](references/patterns/navigation.md)
- 표·목록·검색·필터: [데이터 표시](references/patterns/data-display.md)
- 입력·저장·알림·위험 행동: [폼과 피드백](references/patterns/forms-feedback.md)
- 위계·타이포·간격·색·아이콘·모션: [시각 체계](references/patterns/visual-system.md)
- Apple 원칙을 웹으로 옮길 때: [웹 적용](references/web-adaptation.md), [UI 키트와 아이콘](references/ui-kits-and-symbols.md)
- 최신 정책/자산 권한 확인: [공식 출처](references/sources.md). 인터넷 없이도 위 실행 규칙으로 진행하고 최신성 미확인을 기록한다.
- 사용자가 적법한 자료를 제공한 경우에만: [로컬 자료](references/local-assets.md)

## 경계
공개 패키지는 자체 지침·템플릿·링크만 포함한다. Apple 원문·Sketch/Figma·추출 데이터·폰트·기호·스크린샷은 포함하지 않는다. SF Symbols/브랜드 자산의 웹 재배포 권한을 가정하지 않는다. CSS blur는 Apple Liquid Glass 구현과 같지 않다. native pt와 CSS px를 구분하고 자체 권장값을 Apple 의무값으로 표현하지 않는다. WCAG/GxP 인증, 자동 UI 품질 보장은 제공하지 않는다.
