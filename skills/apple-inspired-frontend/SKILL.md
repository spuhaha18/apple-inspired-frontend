---
name: apple-inspired-frontend
description: Use when designing frontend UI or writing DESIGN.md.
---

# Apple-inspired frontend

Apple HIG를 참고해 프로젝트별 프론트엔드 명세를 만드는 독립적인 커뮤니티 스킬이다. Apple 공식 제품이나 승인된 UI 라이브러리가 아니다.

## 작업 순서
1. 대상 사용자·핵심 업무·웹/네이티브·입력 방식·기존 디자인 시스템을 확인한다. 현재 프로젝트 요구와 승인된 브랜드를 우선한다.
2. [공식 출처](references/sources.md)에서 layout, typography, color, materials, accessibility를 확인한다. 웹 조회가 불가능하면 최신성을 검증하지 못했다고 밝힌다.
3. [웹 적용](references/web-adaptation.md), [UI 키트와 아이콘](references/ui-kits-and-symbols.md)을 읽고 관련 원칙만 적용한다. 전체 공식 사이트를 한 번에 읽지 않는다.
4. [DESIGN 템플릿](templates/DESIGN.md)을 프로젝트 루트 DESIGN.md로 구체화한다. 기존 파일은 읽고 병합한다. 빈 항목을 근거 없이 채우지 않는다. 화면 구조·상태·토큰을 사용자와 합의한 뒤 구현한다.
5. 프로젝트 스택과 컴포넌트 체계를 유지하며 구현한다. Apple native pt와 웹 CSS px, 시각 크기와 활성 영역을 구분한다.
6. [검토 체크리스트](references/review-checklist.md)에 실행 결과와 미검증 사항을 기록한다. DOM/자동 테스트만으로 시각·접근성 검증 완료를 선언하지 않는다.

## 자료 경계
공개 패키지에는 Apple 원문, Sketch/Figma 파일, 추출 JSON, 폰트·기호·스크린샷이 없다. 공식 링크와 자체 작성 가이드만 제공한다. UI 키트 내부가 필요하면 사용자가 적법하게 확보한 파일을 별도 로컬 자료로 제공해야 한다. [로컬 자료 확인](references/local-assets.md)을 따른다.
Liquid Glass는 일반 콘텐츠 전체를 꾸미는 효과가 아니다. CSS blur는 Apple 구현과 동일하지 않다. SF Symbols 자산과 Apple 브랜드 자산은 웹 재배포 가능하다고 가정하지 않는다. 규제 적합성은 이 스킬로 보장하지 않는다.
