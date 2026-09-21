# Apple HIG → 웹 적용

## 공식 원칙 (한국어 자체 요약; 공식 번역 아님)
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout): 중요도별 배치, 정렬·그룹화, 점진적 공개, 크기·언어·텍스트 변화에 대한 적응.
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography): 가독성, 제한된 서체, 굵기·크기 위계, 확대 시 구조 유지.
- [Color](https://developer.apple.com/design/human-interface-guidelines/color): 의미에 일관된 색, 색 외의 상태 표현, 라이트·다크·대비 고려.
- [Materials](https://developer.apple.com/design/human-interface-guidelines/materials): Liquid Glass는 콘텐츠 위의 기능 계층. 일반 콘텐츠에 적용하지 않으며 표준 material과 구분. 활성화되는 일시적 컨트롤 예외는 원문 참조.
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility): 지각 가능하고 적응 가능한 인터페이스, 확대·대체 표현·사용자 설정 지원.

## 웹 시작값 — Apple 공식 수치가 아닌 자체 제안
- 폰트: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. 한글은 OS 기본 또는 라이선스를 확인한 서체. SF Pro 파일을 웹폰트로 재배포하지 않는다.
- 본문 1rem / line-height 1.5, 보조 정보 0.875rem부터 검토. 작은 글자에 얇은 굵기를 피한다.
- 간격 4/8/12/16/24/32/48px, 반경 8/12/16px부터 검토한다. HIG 의무값이 아니다.
- 의미 토큰: background/surface/text/text-muted/border/accent/danger/success/focus. 라이트·다크 및 상태별 실제 조합 대비 측정 후 확정한다.
- 아이콘은 라이선스가 맞는 SVG 세트를 선택하고 동작 아이콘에 접근 가능한 이름을 제공한다.
- 터치 중심이면 44×44 CSS px 정도의 활성 영역을 프로젝트 목표로 검토한다. Apple native pt 규정 또는 WCAG 최소치와 같다고 표현하지 않는다.
- breakpoint는 콘텐츠 기반. 360/768/1280px은 테스트 뷰포트 예시일 뿐이다.
- 짧고 기능적인 전환. `prefers-reduced-motion`에서 비필수 애니메이션 제거. Apple 공통 duration이 있다고 주장하지 않는다.
- 기본은 불투명 surface. 필요하면 탐색 영역에 제한적 blur와 `@supports` fallback. 고대비/forced-colors 및 투명도 감소 옵션을 고려하며 지원 불확실한 media query 하나에 의존하지 않는다.

## 업무/QMS
흐름·밀도·명확한 상태가 장식보다 우선이다. 표의 정렬·필터·빈 결과·페이지 처리·열 제목을 설계한다. 저장/제출/승인/서명을 구분하고 비가역 동작에 확인을 둔다. 규제 적합성·감사추적·전자서명은 이 디자인 가이드로 보장되지 않는다.

## 접근성
[WCAG 2.2](https://www.w3.org/TR/WCAG22/) AA를 웹 검증 목표로 검토한다. 일반 본문 4.5:1, 큰 텍스트 3:1 등 해당 기준과 예외를 원문 대조해 측정한다. HIG native pt 표를 웹 large-text 판정에 그대로 적용하지 않는다. 키보드·포커스·label·오류 연결·스크린리더·확대/리플로우를 수동 검증한다. 자동 검사만으로 적합성을 선언하지 않는다.

## 자산·공유
공식 문서 저작권은 Apple에 있다. 수집은 내부 참조 목적이며 공개 미러/재배포 권한을 뜻하지 않는다. SF Symbols/폰트/Figma 템플릿 등의 이용 조건은 별도 확인한다. 외부 공유는 원문 링크와 자체 요약 중심으로 한다.
