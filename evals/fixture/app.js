// Synthetic local fixture: no network or private data.
const items = ['가상 기획 검토', '가상 일정 확인', '가상 결과 공유'];
const search = document.querySelector('#search');
function render() {
  const matches = items.filter(item => item.includes(search.value.trim()));
  document.querySelector('#results').replaceChildren(...matches.map(item => {
    const li = document.createElement('li'); li.textContent = item; return li;
  }));
  document.querySelector('#count').textContent = matches.length ? `${matches.length}개 결과` : '검색 결과 없음';
}
search.addEventListener('input', render);
document.querySelector('#note-form').addEventListener('submit', event => {
  event.preventDefault();
  document.querySelector('#feedback').textContent = '데모 저장 실패: 입력은 유지됩니다. 다시 시도하세요.';
});
render();
