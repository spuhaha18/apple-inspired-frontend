# 수정 전 기준선 — 2026-09-27

SKILL 수정 전에 고정 small-change 과제를 새 project 디렉터리에서 실행했다. 원시 응답/명령/시간/버전/전체 project 복사본은 Git 제외 `evals/local-runs/`에 있다. 공개 요약은 원문 전체가 아니다.

## 관찰 (실패를 꾸미지 않음)
- Claude none: exit 0, 실제 HTML/CSS/JS 수정. “승인된 DESIGN.md가 없으니 새 설계 문서는 만들지 않았습니다.” 브라우저/셸 미실행을 명시. 브랜드 유지와 비례적인 범위 판단은 이미 충족했다.
- Claude current: exit 0, 실제 수정. “이미 승인된 작은 변경이라 DESIGN.md는 만들지 않았습니다.” 현행판의 전체 DESIGN 단계를 상황에 맞춰 생략했다. 따라서 ‘현행판이 반드시 전체 설계를 강요한다’는 가설은 이 표본에서 반증되었다.
- 두 실행 모두 루트에는 app.js/index.html/style.css뿐이었다. 수정 범위·상태·검증·승인 근거를 다음 세션이 읽을 **CHANGE 산출물**은 없었다. v2에서 다룰 구체적 차이는 전면 설계 강제가 아니라 작은 변경의 간결한 영속 인계 계약이다.
- current 응답은 도구가 Read/Edit/Write뿐인데 “대비는 두 색상 값으로 계산해 약 8:1”이라고 했다. 실제 계산 명령/결과는 제공되지 않았다. 이를 측정 PASS로 인정하지 않는다. 검증 템플릿에 실행 방법과 결과 슬롯을 둔다.
- 모델은 두 응답의 modelUsage에서 `claude-opus-5-5[1m]` (canonical `claude-opus-5-5`). 모델을 지정/변경하지 않았다.
- Codex none/current도 수정 전에 시도했다. 두 실행 exit 1; 원시 응답에 근거해 실패 상세는 results 문서에 기록한다. 실패한 실행은 행동 기준선으로 채점하지 않는다.

## 해석 한계
단일 표본이므로 인과/분산 추정 없음. 5회 이상 wording micro-test와 네 과제 반복 비교는 실행하지 않았다. 현재 지침을 읽도록 한 명시 경로 테스트이며 자동 발견 성공 증거가 아니다. no-guidance는 해당 패키지를 제공하지 않은 조건이지 사용자의 모든 전역 환경을 제거한 조건이 아니다.

## 테스트 먼저
checker가 없는 상태에서 unit tests를 실행: 8 failures, 공통 사유 `checker is not implemented yet`. 이후 checker를 추가하고 실제 현행 패키지의 누락을 검사한 뒤 SKILL을 수정한다.
