# 제한된 실제 평가

[기준선](baseline.md) · [평가 기준](rubric.md) · [실제 결과](results.md)

`fixture/`는 직접 작성한 가상 HTML/CSS/JS다. 의존성/외부 네트워크가 없다. 브라우저에서 index.html을 직접 열 수 있지만 테스트 러너는 브라우저를 설치하거나 UI 검사 성공을 추정하지 않는다.

## 실행
저장소 루트, Python 3.10+와 이미 설치/인증된 CLI에서 실행한다. 각 label은 새 디렉터리를 만들며 재사용하면 실패한다.

```sh
python3 evals/run_pilot.py claude none --label fresh-none --seconds 150
python3 evals/run_pilot.py claude v2 --label fresh-v2 --seconds 180
python3 evals/run_pilot.py codex v2 --label fresh-codex --seconds 180
```

`current`는 호출 시점 폴더를 복사한다. 역사적 현행판 비교에는 반드시 `--skill-source`로 동결한 **이전** 스킬 폴더를 전달한다. 이번 실행의 frozen current는 `local-runs/claude-current/project/.claude/skills/apple-inspired-frontend/`다. 무심코 v2를 current로 다시 채점하지 않는다.

runner는 고정 small-change 프롬프트만 실행한다. 나머지 세 과제는 후속 비교용이며 실행했다고 주장하지 않는다. 12 turns/2 USD(Claude CLI 보고 비용 상한 옵션), 외부 150–180초 제한을 둔다. Codex는 외부 timeout과 workspace-write sandbox를 사용하며 브라우저/설치/네트워크를 과제에서 금지한다. 이 지시는 OS 네트워크 차단 보장이 아니다. CLI 내부 자동 재연결은 raw에 남긴다.

승인된 기존 프록시를 쓸 때만 `--cliproxy`를 추가한다. 호출 환경에 `CLIPROXY_BASE_URL`, `CLIPROXY_API_KEY`, 실제 `/models`에서 확인한 `EVAL_CODEX_MODEL`이 있어야 한다. 키는 argv/파일에 쓰지 않는다. 별도 `local-runs/<label>/codex-home`과 호출 한정 provider 설정을 사용하고 전역 설정은 건드리지 않는다. 기본값/자격증명을 자동 복구하거나 샌드박스를 해제하지 않는다.

## 증거와 공개 경계
`local-runs/`는 Git 제외: prompt.txt, record.json, help.txt, stdout.raw, stderr.raw, project/ 결과가 있다. raw에는 개인 경로가 있어 공개물에 포함하지 않는다. 공개 요약은 자체 작성한 results.md와 증거 메타데이터만 포함한다. 원시 기록은 정제 전 공개하지 않는다. 도구 출력/usage는 제공된 값 그대로이며 추정 비용을 청구 금액으로 해석하지 않는다.

모든 검증 도구는 설치 패키지 밖에 있다. 패키지는 오프라인 Markdown만으로 사용 가능하다. 구조 검사: `python3 scripts/check_package.py`; 단위 검사: `python3 -m unittest discover -s tests -v`.
