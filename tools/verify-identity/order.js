/* Home page order at 320/390/1024 px, wording unchanged, jump link, no overflow in six themes (AC-1.x).
   Run from the repo root with Playwright on NODE_PATH:  node tools/verify-identity/order.js
   Set SHOTS=<dir> to also write per-theme screenshots (treatments only). Dev-only; the page never loads this. */
const {chromium}=require('playwright');
const FILE='file://'+require('path').resolve(__dirname,'..','..','index.html');
const CHROMIUM=process.env.PW_CHROMIUM||'/opt/pw-browsers/chromium';let fail=0;const ok=(c,m)=>{console.log((c?'ok   ':'FAIL ')+m);if(!c)fail++};
const THESIS='Six regions own the roof of the continent. The snow that lands on them becomes the Columbia, the Missouri, the Colorado, the Rio Grande, the Saskatchewan, and the Mackenzie — and a tangle of compacts, treaties, and Supreme Court decrees decides who drinks it. Tap a region to open its ledger, or search for a river.';
const IDS=['survey-light','survey-night','docket-light','docket-night','poster-light','poster-night'];
(async()=>{const b=await chromium.launch({executablePath:CHROMIUM});const errs=[];
for(const w of [320,390,1024]){const c=await b.newContext({viewport:{width:w,height:w===1024?800:844}});const p=await c.newPage();p.on('pageerror',e=>errs.push(e.message));await p.goto(FILE);await p.waitForSelector('.lead-stats');
const y=await p.evaluate(()=>{const t=s=>{const e=document.querySelector(s);return e?e.getBoundingClientRect().top+scrollY:null};return {h1:t('h1'),search:t('#siteSearch'),map:t('.map-card'),th:t('.thesis'),st:t('.lead-stats'),jump:t('#leadJump'),ch:t('#contCard'),vh:innerHeight}});
ok(y.h1<y.search&&y.search<y.map,'@'+w+' title, search, map order');ok(y.map<y.vh,'@'+w+' map top visible ('+Math.round(y.map)+' < '+y.vh+')');ok(y.map<y.th&&y.th<y.st&&y.st<y.jump&&y.jump<y.ch,'@'+w+' intro, stats, jump link, chart follow the map in order');
if(w===390){const t=await p.evaluate(()=>{const st=e=>{const c=e.cloneNode(true);c.querySelectorAll('.deco').forEach(n=>n.remove());return c.textContent.replace(/\s+/g,' ').trim()};return {th:st(document.querySelector('.thesis')),s:[...document.querySelectorAll('.ls')].map(st),j:document.querySelector('#leadJump').textContent.trim(),n:document.querySelectorAll('.thesis').length}});
ok(t.th===THESIS&&t.n===1,'intro wording unchanged, not duplicated');ok(/^85%\s*of the water goes to just two places: the Pacific Ocean and the Arctic Ocean$/.test(t.s[0])&&/^2\.1%\s*is carried by the Colorado — the river the 2026 fight is about$/.test(t.s[1]),'stats wording + live values');ok(t.j==='See where it all ends up ↓','jump wording');
await p.click('#leadJump');let l=true;try{await p.waitForFunction(()=>Math.abs(document.getElementById('contCard').getBoundingClientRect().top)<8,null,{timeout:4000})}catch(e){l=false}ok(l,'jump link scrolls to continental chart');
for(const id of IDS){await p.evaluate(i=>{scrollTo(0,0);document.querySelector('.theme-dot[data-set="'+i+'"]').click()},id);const o=await p.evaluate(()=>[document.documentElement.scrollWidth,innerWidth]);ok(o[0]<=o[1],id+' no horizontal scroll');}}
await c.close()}
ok(errs.length===0,'no page errors '+(errs[0]||''));await b.close();console.log(fail?fail+' FAILED':'ALL OK');process.exit(fail?1:0)})()
