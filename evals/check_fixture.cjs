#!/usr/bin/env node
// Deterministic event-logic probe, NOT a browser/DOM/layout accessibility test.
// Minimal stand-ins only for APIs used by the synthetic fixture.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const project = process.argv[2];
assert(project, 'usage: node evals/check_fixture.cjs PROJECT');
const html = fs.readFileSync(path.join(project, 'index.html'), 'utf8');
const elements = {};
let focused = null;
function element(id) {
  return {id, value: '', textContent: '', children: [], listeners: {},
    addEventListener(event, callback) {this.listeners[event] = callback;},
    replaceChildren(...children) {this.children = children;},
    focus() {focused = this.id;},
  };
}
for (const match of html.matchAll(/id="([^"]+)"/g)) elements[match[1]] = element(match[1]);
const document = {
  querySelector(selector) {return elements[selector.slice(1)] || null;},
  getElementById(id) {return elements[id] || null;},
  createElement(tag) {return element(tag);},
};
vm.runInNewContext(fs.readFileSync(path.join(project, 'app.js'), 'utf8'), {document}, {timeout: 1000});
assert.equal(elements.results.children.length, 3, 'initial results');
elements.search.value = '기획'; elements.search.listeners.input();
assert.equal(elements.results.children.length, 1, 'matching search');
elements.search.value = '없는문서'; elements.search.listeners.input();
assert.equal(elements.results.children.length, 0, 'empty result');
const clear = elements['clear-search'];
assert(clear, 'clear-search button must exist');
assert.equal(typeof clear.listeners.click, 'function', 'clear listener');
clear.listeners.click();
assert.equal(elements.search.value, '', 'clear value');
assert.equal(elements.results.children.length, 3, 'restore all results');
assert.equal(focused, 'search', 'focus call returns to search');
elements.note.value = '가상 메모';
let prevented = false;
elements['note-form'].listeners.submit({preventDefault(){prevented = true;}});
assert(prevented, 'form default prevented');
assert.equal(elements.note.value, '가상 메모', 'note preserved');
assert(elements.feedback.textContent.includes('실패'), 'demo failure preserved');
console.log('PASS: initial/matching/empty/clear/restore/focus-call/note-preservation event logic. Browser/layout/screen-reader NOT tested.');
