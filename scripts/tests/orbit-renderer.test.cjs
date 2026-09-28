// Run: node scripts/tests/orbit-renderer.test.cjs
// Executes the actual page script with a minimal DOM/canvas test double.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname, '../../visualizations/6d-orbit-slice.html'), 'utf8');
const source = html.slice(html.indexOf('(() => {'), html.lastIndexOf('</script>'));
let frame, lines = [], arcs = [], current, resizeCallback, now = 0;
let stageSize = {width: 800, height: 620};
const ctx = {
  setTransform() {}, clearRect() { lines = []; arcs = []; },
  beginPath() { current = []; }, moveTo(x,y) { current.push([x,y]); },
  lineTo(x,y) { current.push([x,y]); }, stroke() { lines.push(current); },
  arc(x,y,r) { assert.ok([x,y,r].every(Number.isFinite)); arcs.push([x,y,r]); }, fill() {}
};
function element(value) {
  return { value, events: {}, addEventListener(kind, callback) { this.events[kind] = callback; }, setAttribute() {} };
}
const elements = Object.fromEntries(['depth','imbalance','phaseOffset','responsePower','responseNote','imbalanceValue','orbitCondition','stateReturn','phaseReadout','orbitLabel','resetOrbit','resetView','alignExtraOne','alignExtraTwo'].map(id => [id, element()]));
elements.depth.value = html.match(/id="depth"[^>]*value="([^"]+)"/)[1];
assert.equal(elements.depth.value, '0.64', 'Default observer height is doubled'); elements.imbalance.value = '0'; elements.phaseOffset.value = '0'; elements.responsePower.value = '0.5';
elements.orbitStage = {getBoundingClientRect: () => stageSize};
elements.orbitCanvas = {...element(), style: {}, getContext: () => ctx, setPointerCapture() {}};
const buttons = [0,1,2,3].map(l => ({...element(), dataset: {l: String(l)}}));
vm.runInNewContext(source, {
  document: {getElementById: id => { assert.ok(elements[id], id); return elements[id]; }, querySelectorAll: () => buttons},
  window: {devicePixelRatio: 1, addEventListener() {}},
  performance: {now: () => now}, requestAnimationFrame: callback => { frame = callback; }, Math, Number,
  ResizeObserver: class {
    constructor(callback) { resizeCallback = callback; }
    observe(target) { assert.equal(target, elements.orbitStage); }
  }
});
function select(l) { buttons[l].events.click(); }
function change(id, value, event) { elements[id].value = value; elements[id].events[event](); }
function radii() { return lines.slice(1).flat().map(([x,y]) => Math.hypot((x-400)/(620*.37), (y-310)/(620*.37))); }
for (let l=0; l<=3; l++) {
  select(l); frame(1000);
  assert.equal(lines.length, 1401);
  const r = radii(); assert.ok(r.every(Number.isFinite));
  assert.ok(Math.max(...r) > .999);
  assert.ok(l === 0 ? Math.min(...r) > .999 : Math.min(...r) < .01);
  assert.match(elements.stateReturn.textContent, /100.00% \(full state recurs\)/);
}
select(1); change('imbalance', '.6', 'input'); frame(1000);
assert.ok(Math.abs(Math.min(...radii()) - .6/Math.hypot(1,.6)) < .002);
assert.match(elements.stateReturn.textContent, /not a full state recurrence/);
frame(8499); const before = arcs.at(-1);
frame(8501); const after = arcs.at(-1);
assert.ok(Math.hypot(before[0]-after[0], before[1]-after[1]) < 2, 'No forced clock-turn jump');
elements.resetOrbit.events.click(); frame(1000);
const ideal = JSON.stringify(lines);
change('phaseOffset', '.5', 'change'); frame(1000);
assert.equal(JSON.stringify(lines), ideal, 'Offset must not alter visible geometry');
assert.match(elements.stateReturn.textContent, /7.84%/);
frame(17000); assert.match(elements.phaseReadout.textContent, /current state return: 100.0%/);
change('phaseOffset', 'sqrt2', 'change'); frame(1000);
assert.equal(JSON.stringify(lines), ideal);
assert.match(elements.stateReturn.textContent, /prevents exact state recurrence/);
const expected = 100*(.36*.36+.64*.64+2*.36*.64*Math.cos(2*Math.PI*Math.SQRT2));
assert.ok(elements.stateReturn.textContent.includes(expected.toFixed(2)+'%'));
select(0); assert.ok(elements.imbalance.disabled && elements.phaseOffset.disabled);
frame(1000); assert.ok(Math.min(...radii()) > .999);
elements.resetOrbit.events.click(); select(3); frame(1000);
assert.equal(elements.imbalance.value, '0'); assert.equal(elements.phaseOffset.value, '0');
assert.ok(Math.min(...radii()) < .01);
for (const l of [1,2,3]) {
  select(l); elements.resetOrbit.events.click();
  elements.alignExtraOne.events.click();
  assert.ok(Math.abs(Number(elements.imbalance.value)-Math.sqrt(l+.25)) < 1e-12);
  assert.match(elements.stateReturn.textContent, /7.84%/);
  assert.match(elements.stateReturn.textContent, /recurs after two turns/);
  assert.ok(elements.orbitCondition.textContent.includes(`${2*l+1} radial maxima`));
  frame(17000); assert.match(elements.phaseReadout.textContent, /current state return: 100.0%/);
  change('phaseOffset', '.5', 'change');
  assert.match(elements.stateReturn.textContent, /100.00% \(full state recurs\)/);
  change('phaseOffset', '0', 'change'); elements.alignExtraTwo.events.click();
  assert.ok(Number(elements.imbalance.value) <= 3);
  assert.ok(Math.abs(Number(elements.imbalance.value)-Math.sqrt(2*l+1)) < 1e-12);
  assert.match(elements.stateReturn.textContent, /100.00% \(full state recurs\)/);
  assert.ok(elements.orbitCondition.textContent.includes(`${2*l+2} radial maxima`));
  frame(1000); assert.ok(Math.min(...radii()) > .1);
}
// A readout change preserves the state but squares both resolved amplitudes.
select(1); elements.resetOrbit.events.click();
change('imbalance', '.6', 'input');
const originalState = elements.stateReturn.textContent;
change('responsePower', '1', 'change'); frame(1000);
assert.ok(Math.abs(Math.min(...radii()) - .36/1.36) < .002, 'Smooth readout has q, not sqrt(q), radius');
assert.equal(elements.stateReturn.textContent, originalState, 'Detector response does not change the state');
assert.match(elements.responseNote.textContent, /Smooth/);
assert.match(elements.orbitCondition.textContent, /0.265 R/);
elements.resetOrbit.events.click();
function headAt(theta) {
  frame(theta/(2*Math.PI)*8500);
  const [x,y] = arcs.at(-1);
  return [(x-400)/(620*.37), (y-310)/(620*.37)];
}
const center = Math.PI/2, h = 1e-4;
for (const beta of ['0.5','1']) {
  change('responsePower', beta, 'change');
  const before = headAt(center-h), at = headAt(center), after = headAt(center+h);
  const jump = Math.hypot(...at.map((v,i) => (after[i]-2*v+before[i])/h));
  assert.ok(beta === '1' ? jump < .001 : Math.abs(jump-2) < .001, 'Smooth response removes the planar velocity corner');
  // Rotate the depth axis into view and check its zero at theta=pi too.
  elements.orbitCanvas.events.pointerdown({pointerId:1,clientX:0,clientY:0});
  elements.orbitCanvas.events.pointermove({pointerId:1,clientX:Math.PI/2/.008,clientY:0});
  elements.orbitCanvas.events.pointerup({pointerId:1});
  const a = headAt(Math.PI-h), b = headAt(Math.PI), c = headAt(Math.PI+h);
  const depthJump = Math.hypot(...b.map((v,i) => (c[i]-2*v+a[i])/h));
  assert.ok(beta === '1' ? depthJump < .001 : Math.abs(depthJump-2*Number(elements.depth.value)) < .001, 'Smooth response removes the depth velocity corner');
  elements.resetView.events.click();
}
change('responsePower', '0.5', 'change');
select(0); assert.ok(elements.alignExtraOne.disabled && elements.alignExtraTwo.disabled);
elements.resetOrbit.events.click(); select(3);
assert.ok(html.indexOf('<figure class="orbit-lab">') < html.indexOf('<article class="orbit-prose">'));
assert.match(html, /grid-template-areas: "prose visual"/);
assert.match(html, /grid-template-areas: "visual" "prose"/);
assert.match(html, /aspect-ratio: 1 \/ 1/);
assert.match(html, /<details class="lab-details">/);
assert.match(html, /flex-wrap: nowrap/);
assert.match(html, /height: 26px; min-height: 26px/);
assert.match(html, /aria-label="L = 0, ring"[^>]*>L0<\/button>/);
assert.match(html, /<select id="phaseOffset"[^>]*><option value="0">0<\/option>/);
assert.match(html, /max-height: 35%/);
assert.match(html, /max-height: 40%/);
assert.match(html, /id="imbalance"[^>]*max="3"[^>]*step="any"/);
for (const size of [{width: 360, height: 175}, {width: 680, height: 410}]) {
  stageSize = size; resizeCallback(); frame(1000);
  assert.equal(elements.orbitCanvas.width, size.width);
  assert.equal(elements.orbitCanvas.height, size.height);
  assert.equal(lines.length, 1401);
  assert.ok(arcs.every(([x,y]) => Number.isFinite(x+y)));
}
console.log('PASS: ideal ring/petals, imbalance floor, continuous clock crossing, invisible phase, ray recurrence, ring guard, and reset.');
console.log('PASS: responsive DOM order and layout declarations; canvas follows panel resizes without losing the trajectory.');
console.log('PASS: exact extra-maximum alignments beyond the old range, one/two-turn recurrence, and phase-offset interaction.');

console.log('PASS: smooth response preserves the state, gives the correct radius floor, and removes planar and depth velocity corners.');

select(1); elements.resetOrbit.events.click();
change('phaseOffset', '.5', 'change');
now = 3000; frame(now);
const phaseBeforeResponse = elements.phaseReadout.textContent;
change('responsePower', '1', 'change'); frame(now);
assert.equal(elements.phaseReadout.textContent, phaseBeforeResponse, 'Changing the response must preserve the running clock and state');
console.log('PASS: changing the position response preserves the current motion phase.');
