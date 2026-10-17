/* Per-theme fonts load offline, no outside requests, map labels keep system mono, Survey/Docket/Poster decorations (AC-2.5, 3.x, 4.x).
   Run from the repo root with Playwright on NODE_PATH:  node tools/verify-identity/treatments.js
   Set SHOTS=<dir> to also write per-theme screenshots (treatments only). Dev-only; the page never loads this. */
const {chromium}=require('playwright');
const FILE='file://'+require('path').resolve(__dirname,'..','..','index.html');
const CHROMIUM=process.env.PW_CHROMIUM||'/opt/pw-browsers/chromium';
const T={'survey-light':['Big Shoulders Display','Barlow Semi Condensed','IBM Plex Mono'],'survey-night':['Big Shoulders Display','Barlow Semi Condensed','IBM Plex Mono'],'docket-light':['Special Elite','Libre Caslon Text','Cutive Mono'],'docket-night':['Special Elite','Libre Caslon Text','Cutive Mono'],'poster-light':['Alfa Slab One','Zilla Slab','Zilla Slab'],'poster-night':['Alfa Slab One','Zilla Slab','Zilla Slab']};
let fail=0;const ok=(c,m)=>{console.log((c?'ok   ':'FAIL ')+m);if(!c)fail++};const ff=s=>s.split(',')[0].replace(/["']/g,'').trim();
(async()=>{const b=await chromium.launch({executablePath:CHROMIUM});const errs=[],out=[];
for(const w of [390,320]){const c=await b.newContext({viewport:{width:w,height:844}});await c.setOffline(true);const p=await c.newPage();p.on('pageerror',e=>errs.push(e.message));p.on('request',r=>{if(!/^(file|data|blob|about):/.test(r.url()))out.push(r.url())});await p.goto(FILE);await p.waitForSelector('.lead-stats');
for(const id of Object.keys(T)){await p.evaluate(i=>document.querySelector('.theme-dot[data-set="'+i+'"]').click(),id);await p.waitForTimeout(200);
const r=await p.evaluate(async()=>{await document.fonts.ready;const cs=(s,q)=>getComputedStyle(document.querySelector(s))[q];const vis=s=>{const e=document.querySelector(s);return !!e&&getComputedStyle(e).display!=='none'&&e.getBoundingClientRect().width>0};
return {h1:cs('h1','fontFamily'),stat:cs('.ls-n','fontFamily'),body:cs('body','fontFamily'),label:cs('.eyebrow','fontFamily'),search:cs('.search-box','fontFamily'),svg:cs('.map-card svg text','fontFamily'),loaded:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family.replace(/["']/g,'')),tr:cs('h1','textTransform'),hb:parseFloat(cs('h1','borderTopWidth')),lsbg:cs('.ls','backgroundColor'),bm:vis('.ls-tag-bm'),fi:vis('.ls-tag-finding'),st:vis('.deco-stamp'),cap:vis('.deco-cap'),sw:document.documentElement.scrollWidth,iw:innerWidth}});
const [t,bd,lb]=T[id];
if(w===390){ok(ff(r.h1)===t&&ff(r.stat)===t,id+' title+stat font '+t);ok(ff(r.body)===bd&&ff(r.search)===bd,id+' body+search font '+bd);ok(ff(r.label)===lb,id+' label font '+lb);ok([t,bd,lb].every(f=>r.loaded.includes(f)),id+' fonts loaded offline');ok(/monospace/.test(r.svg)&&!/Plex|Cutive|Zilla|Barlow|Big Sh|Elite|Alfa|Caslon/.test(r.svg),id+' map labels keep system mono');
const d=id.split('-')[0];if(d==='survey')ok(r.bm&&!r.fi&&!r.st&&r.tr==='uppercase','AC-3.1 '+id);if(d==='docket')ok(r.fi&&r.st&&r.cap&&!r.bm,'AC-3.2 '+id);if(d==='poster')ok(r.hb>=2&&r.lsbg!=='rgba(0, 0, 0, 0)'&&!r.bm&&!r.fi&&!r.st,'AC-3.3 '+id);
if(process.env.SHOTS)await p.screenshot({path:process.env.SHOTS+'/'+id+'.png'})}
ok(r.sw<=r.iw,id+' @'+w+' no horizontal scroll ('+r.sw+'/'+r.iw+')')}await c.close()}
ok(errs.length===0,'no page errors '+(errs[0]||''));ok(out.length===0,'no outside requests');await b.close();console.log(fail?fail+' FAILED':'ALL OK');process.exit(fail?1:0)})()
