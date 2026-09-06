// Run: node scripts/tests/orbit-renderer.test.cjs
// Executes the actual page script with a minimal DOM/canvas test double.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname, '../../visualizations/6d-orbit-slice.html'), 'utf8');
const source = html.slice(html.indexOf('(() => {'), html.lastIndexOf('</script>'));
let frame, lines = [], arcs = [], current;
const ctx = {
  setTransform() {}, clearRect() { lines = []; arcs = []; },
  beginPath() { current = []; }, moveTo(x,y) { current.push([x,y]); },
  lineTo(x,y) { current.push([x,y]); }, stroke() { lines.push(current); },
  arc(x,y,r) { assert.ok([x,y,r].every(Number.isFinite)); arcs.push([x,y,r]); }, fill() {}
};
function element(value) {
  return { value, events: {}, addEventListener(kind, callback) { this.events[kind] = callback; }, setAttribute() {} };
}
const elements = Object.fromEntries(['depth','imbalance','phaseOffset','imbalanceValue','orbitCondition','stateReturn','phaseReadout','orbitLabel','resetOrbit','resetView'].map(id => [id, element()]));
elements.depth.value = '.32'; elements.imbalance.value = '0'; elements.phaseOffset.value = '0';
elements.orbitStage = {getBoundingClientRect: () => ({width: 800, height: 620})};
elements.orbitCanvas = {...element(), style: {}, getContext: () => ctx, setPointerCapture() {}};
const buttons = [0,1,2,3].map(l => ({...element(), dataset: {l: String(l)}}));
vm.runInNewContext(source, {
  document: {getElementById: id => { assert.ok(elements[id], id); return elements[id]; }, querySelectorAll: () => buttons},
  window: {devicePixelRatio: 1, addEventListener() {}},
  performance: {now: () => 0}, requestAnimationFrame: callback => { frame = callback; }, Math, Number
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
console.log('PASS: ideal ring/petals, imbalance floor, continuous clock crossing, invisible phase, ray recurrence, ring guard, and reset.');
