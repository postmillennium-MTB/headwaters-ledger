/* Picker, default, saved-theme fallback, persistence, blocked storage, chrome color, contrast, 320/390 px overflow (spec AC-2.x, 5.x, 6.x).
   Run from the repo root with Playwright on NODE_PATH:  node tools/verify-identity/themes.js
   Set SHOTS=<dir> to also write per-theme screenshots (treatments only). Dev-only; the page never loads this. */
const {chromium}=require('playwright');
const FILE='file://'+require('path').resolve(__dirname,'..','..','index.html');
const CHROMIUM=process.env.PW_CHROMIUM||'/opt/pw-browsers/chromium';
const KEY='pmrHeadwatersTheme';
const IDS=['survey-light','survey-night','docket-light','docket-night','poster-light','poster-night'];
function lum(h){const v=[1,3,5].map(i=>parseInt(h.replace('#','').slice(i-1,i+1),16)/255).map(c=>c<=.03928?c/12.92:Math.pow((c+.055)/1.055,2.4));return .2126*v[0]+.7152*v[1]+.0722*v[2]}
const R=(a,b)=>{const x=Math.max(lum(a),lum(b)),y=Math.min(lum(a),lum(b));return (x+.05)/(y+.05)};
let fail=0;const ok=(c,m)=>{console.log((c?'ok   ':'FAIL ')+m);if(!c)fail++};
(async()=>{const b=await chromium.launch({executablePath:CHROMIUM});const errs=[];
async function open(init,w=390){const c=await b.newContext({viewport:{width:w,height:844}});if(init)await c.addInitScript(init);const p=await c.newPage();p.on('pageerror',e=>errs.push(e.message));await p.goto(FILE);await p.waitForSelector('.lead-stats');return {c,p}}
const th=p=>p.evaluate(()=>document.documentElement.getAttribute('data-theme'));
let {c,p}=await open();
const dots=await p.$$eval('.theme-dot',d=>d.map(x=>x.dataset.set));
ok(dots.length===6&&IDS.every(i=>dots.includes(i)),'six dots, six ids');
ok(await th(p)==='survey-light','default survey-light');
for(const id of IDS){await p.evaluate(i=>document.querySelector('.theme-dot[data-set="'+i+'"]').click(),id);
 const r=await p.evaluate(()=>({t:document.documentElement.getAttribute('data-theme'),meta:document.querySelector('meta[name=theme-color]').content,cs:document.documentElement.style.colorScheme,paper:getComputedStyle(document.documentElement).getPropertyValue('--paper').trim(),sw:document.documentElement.scrollWidth,iw:innerWidth}));
 ok(r.t===id&&r.meta.toLowerCase()===r.paper.toLowerCase()&&r.cs===(id.endsWith('night')?'dark':'light'),id+' switches; chrome color + scheme match');
 ok(r.sw<=r.iw,id+' no horizontal scroll @390');
 const t={};for(const n of ['--paper','--card','--ink','--ink-soft','--river','--canyon','--sage','--basin-pacific','--basin-arctic','--basin-atlantic','--basin-gulfcal','--basin-home','--basin-none'])t[n]=await p.evaluate(n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim(),n);
 const pairs=[['--ink','--paper'],['--ink','--card'],['--ink-soft','--paper'],['--ink-soft','--card'],['--river','--paper'],['--river','--card'],['--canyon','--paper'],['--canyon','--card'],['--sage','--card'],['--paper','--river'],['--paper','--canyon']];
 const bad=pairs.filter(q=>R(t[q[0]],t[q[1]])<4.5).map(q=>q.join('/')+' '+R(t[q[0]],t[q[1]]).toFixed(2));
 const bb=Object.keys(t).filter(k=>k.startsWith('--basin')&&R(t[k],t['--card'])<3).map(k=>k+' '+R(t[k],t['--card']).toFixed(2));
 ok(!bad.length,id+' text contrast >=4.5'+(bad.length?' '+bad:''));ok(!bb.length,id+' basin >=3:1 on card'+(bb.length?' '+bb:''));}
await p.evaluate(()=>document.querySelector('.theme-dot[data-set="docket-night"]').click());await p.reload();await p.waitForSelector('.lead-stats');
ok(await th(p)==='docket-night','chosen theme persists across reload');await c.close();
for(const v of ['snowmelt','canyon','nightflow','survey','bogus','']){({c,p}=await open('try{localStorage.setItem("'+KEY+'","'+v+'")}catch(e){}'));ok(await th(p)==='survey-light','saved "'+v+'" -> survey-light');await c.close()}
({c,p}=await open('try{localStorage.setItem("'+KEY+'","poster-night")}catch(e){}'));ok(await th(p)==='poster-night','saved poster-night honored');await c.close();
({c,p}=await open('Storage.prototype.getItem=function(){throw 1};Storage.prototype.setItem=function(){throw 1}'));ok(await th(p)==='survey-light','blocked storage -> survey-light');
await p.evaluate(()=>document.querySelector('.theme-dot[data-set="docket-light"]').click());ok(await th(p)==='docket-light','picker works with blocked storage');await c.close();
for(const w of [320]){({c,p}=await open(null,w));for(const id of IDS){await p.evaluate(i=>document.querySelector('.theme-dot[data-set="'+i+'"]').click(),id);const o=await p.evaluate(()=>[document.documentElement.scrollWidth,innerWidth]);ok(o[0]<=o[1],id+' @320 no horizontal scroll');}await c.close()}
ok(errs.length===0,'no page errors '+(errs[0]||''));await b.close();console.log(fail?fail+' FAILED':'ALL OK');process.exit(fail?1:0)})()
