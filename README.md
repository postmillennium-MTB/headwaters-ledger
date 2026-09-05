# The Headwaters Ledger

**A single-file interactive tool mapping where water goes from the six headwaters regions of the Rocky Mountains, and who controls it.**

Part of the Post Millennium Renaissance tool suite · `postmillenniumrenaissance.com`

---

## What this actually is

One HTML file (`index.html`). No build step, no install, no dependencies. You open it in a browser and it works — which also means you can drop it straight into a GitHub Pages repo and iframe it into your site or a Pinkbike article, exactly like the other PMR tools.

Everything — every state, every river, every reservoir, every quiz question — lives inside that one file as plain data. There's no database and nothing to configure. To change what the tool says, you (or a future Claude session) find the right paragraph of text inside the file and edit it directly.

## What's in it

**A clickable map** of six regions: Colorado, Wyoming, Montana, Idaho, British Columbia, and Alberta — the "headwaters club," the places where the continent's water is actually born. Click a region, get its own page. A small key at the bottom-left explains the dashed Continental Divide line and points north.

**Two summary cards on the home page**, above the essay:

- **"The West's Water Infrastructure Is Getting Old"** — a bar chart of average reservoir age by state, computed live from each region's reservoir data (not typed in by hand — add or edit a reservoir and the average updates itself).
- **"How Much Stays Home"**, sitting next to the essay card at half-width — a bar chart of what share of each region's annual flow is actually used there versus leaving for somewhere else, pulled directly from the same numbers already driving each region's Ledger Balance pie chart.

**Each region's page has five tabs:**

| Tab | What it shows |
|---|---|
| Where It Goes | An interactive diagram of that region's rivers, which state/province/country each one flows to, and a pie chart of the split — plus which agreement governs each river |
| The Agreements | Every compact, treaty, or court decree that touches that region's water, filterable by "still in force forever" vs. "expiring or in limbo" |
| Countdown 2026 / The Stakes | Colorado gets a live countdown to the Colorado River rule changes — which flips to counting the days *since* each deadline once it passes, so the tab never goes stale; the other five get a "here's what's actually at risk" section |
| Reservoirs | The region's major reservoirs — name, river, year built, capacity — with an average-age callout and combined-capacity stat. Populated for Colorado, Wyoming, Montana, and Idaho so far; British Columbia and Alberta show a "coming soon" card until that data's added |
| Quiz | 4–5 questions per region, multiple choice, with an explanation after each answer |

**One essay**, "Too Heavy, Too Cheap: Why America Pipes Oil and Not Water," reachable from a card on the map page. It answers a question people naturally ask once they've looked at the map: if we pipe oil across the country, why not water?

**Four color themes** (the dots in the top right): Snowmelt (default blue), Canyon (warm/orange), Nightflow (dark mode), Survey (sepia/vintage). These apply everywhere at once, and your choice is remembered between visits.

**A link back to your homepage**, top right, under the theme dots.

**On a phone**, two things change shape rather than just shrinking. The map gains a tappable list of the six regions underneath it, each with the one-line résumé that desktop readers only get by hovering. And each region's river diagram is replaced by a stacked list of the same rivers at readable size — the diagram itself is drawn at a fixed width, so at phone scale its labels came out around four pixels tall. Everything else (back button, browser back gesture, quiz retry, tapping a pie slice and tapping it again to clear) is sized and wired for thumbs.

## How to update it (no coding required, but here's the shape of it)

Because this is one big file, "editing" really means: open the file, use Ctrl+F / Cmd+F to search for a phrase you want to change, and edit the text between the quote marks. A few landmarks to search for:

- To edit a fact or fix a typo in an existing region: search for a distinctive phrase from that sentence (e.g. search `"Kansas sued Colorado"` to jump straight to the Arkansas River entry).
- To add a new quiz question: search for `quiz:[` under the region you want, and copy the pattern of an existing question (the four-line block starting with `{q:`).
- **To add or edit a reservoir**: search for `reservoirs:[` under the region you want. Each entry is `{name, river, yearBuilt, capacityAF, note?}` — `note` is optional. British Columbia and Alberta currently have empty arrays (`reservoirs:[]`); populating those is the most obvious next step, and that's the *whole* edit — the home-page infrastructure-age card now works out which regions have reservoir data by looking at the data itself, so there's no second list to remember to update.
- To add a whole new region (a 7th state, say): that's a bigger job — it means adding a new data block plus a new shape on the map itself. Best done by describing what you want to Claude rather than hand-editing, since the map's shapes need to line up geometrically with each other, and the existing six already fill the available space tightly.
- To add a new essay: same idea as the Too Heavy, Too Cheap essay — a block of content plus a card on the home page. Also best done with Claude's help the first time; after that, editing the *text* of an existing essay is just normal text editing.

**The safest way to make any change**, technical background or not: paste the file to Claude and describe what you want changed in plain English ("Colorado's second quiz question has a typo," "add a sentence to Wyoming's local box about X," "add the BC reservoirs"). Claude can find the exact spot and make the edit without touching anything else — that's how every update to this tool has happened so far.

### Keeping it from looking out of date

The tool is about deadlines, so it has to age gracefully on its own. Three things now do that without anyone editing anything:

- **The Colorado countdown flips tense.** Before a deadline a card reads "26 days until Oct 1, 2026…"; after it, the same card reads "45 days since Oct 1, 2026…" and is marked **Now in force**. It never prints a dead word where a number should be. Each of the two cards decides independently, so between October and December one counts up while the other counts down.
- **The tab renames itself.** It reads "Countdown 2026" while anything is still ahead, and "The 2026 Reckoning" once both dates have passed. The heading and intro paragraph swap the same way.
- **The timeline dots sort themselves.** Each entry carries a machine-readable `iso` date; whether its dot is filled (past) or hollow (future) is worked out on every page load rather than typed in by hand.

The one thing that **does** need a human: **`LAST_REVIEWED`**, near the top of the script. It prints in the footer as "last reviewed September 2026". Bump it whenever you edit content — it's the only signal a reader has that someone is still minding the page.

### For a future Claude session (architecture notes)

The file went through a maintainability pass and a couple of feature rounds after it was first built, so a few things are worth knowing before you dive in:

- **`TOOL_NUMBER`**, near the top of the script, is the single source for the "No. 14" catalog number shown in the eyebrow and on every region's ledger badge (`14-A` through `14-F`). Change it once there, not in the 14 places it used to be hard-typed.
- **`STATES`** is the one data object driving almost everything. There's a schema comment directly above it listing every field a region needs. Everything above the `END OF DATA` marker is content; everything below it is logic.
- **`THEMES`** is the registry for the four color themes. Adding one is a one-line entry plus one CSS palette block — and the registry comment records the CSS specificity trap that decides where that block has to go in the stylesheet. Don't move the default theme's `:root` block without reading it.
- **`TABS`** is the registry for the five per-region tabs. Adding a sixth is a render function plus one line; the button, the panel, the show/hide wiring, and the keyboard navigation all derive from it.
- **`THIRD_TAB`** is a small registry (`{crisis: {...}, stakes: {...}}`) that renders and wires up each region's third tab. Colorado uses `crisis` (the 2026 countdown); the other five use `stakes`. If you ever want a third kind of tab, add a new key here with `render(st)` and `wire(st)` functions — you won't need to touch `renderState()` itself.
- **`reservoirSummary()`** and **`barListHtml()`** are shared helpers — the first averages a region's reservoir data once so the per-region Reservoirs tab and the home-page infrastructure card can never disagree with each other; the second is a small reusable bar-chart renderer (built on the `.bars`/`.bartrack`/`.barfill` CSS already used by Colorado's countdown-math widget) used by both new home-page cards.
- **The home-page "How Much Stays Home" card** reads a `home:true` flag on the relevant pie slice in each region's data. It used to pattern-match the slice's *display label* for the words "Stays in…", which meant a harmless prose edit could silently drop a region to "<1%".
- **`escapeHtml()`** exists specifically for reservoir data pulled from outside sources (Wikipedia, dam-operator sites). The rest of the file's prose fields (`thesis`, `text`, etc.) intentionally contain hand-authored HTML like `<b>` and `<span class="flow">` for styling — don't wrap those in `escapeHtml()`, it'll break the formatting.
- **The flow diagram has two layouts, not one.** The "Where It Goes" SVG is desktop-only; below 700px CSS hides it and shows `flowList()` — the same rivers as a stacked list of real buttons at readable font size. Both are always in the DOM and share one selection handler, so they can't disagree. **Do not** try to fix mobile by shrinking the SVG's viewBox: that was tried and reverted, because the longest river name and the longest destination label collide at narrower widths. That trap is recorded in a comment above `flowSvg()`.
- **The diagram's width is computed, not typed.** `FLOW_W` is derived from the longest destination label across all six regions. At the old hard-coded 900 units, Wyoming's Bear River label ran off the right edge and was silently clipped — SVG raises no error when content overflows its viewBox, so that kind of bug ships quietly.

## Deployment

Same pattern as your other PMR tools:

1. Commit `index.html` to the tool's GitHub repo (watch out for the known GitHub-web-UI issue where it sometimes creates a new branch instead of committing straight to `main` — double check before you navigate away).
2. GitHub Pages serves it automatically.
3. Iframe it into `postmillenniumrenaissance.com` or a Pinkbike article the way you do with the rest of the tools grid.

### Two things the iframe needs

- **The homepage link is `target="_top"`.** Without it, clicking `postmillenniumrenaissance.com` in the top right loads your whole site *inside* the tool's own embed frame, with no way back out. This is easy to break by accident and invisible until someone clicks it on the live site.
- **Deep links can be handed in from the wrapper page.** A `#co` on the outer page's URL can never be read from inside a cross-origin iframe. The tool now listens for a `postMessage` of the shape `{type:'pmr-hash', hash:'#co'}` and switches to that region — but only from `postmillenniumrenaissance.com`, checked against an allowlist. The wrapper page can either post that message or just append the hash to the iframe `src`; either works.

### Social previews

The `og:` and `twitter:` tags in the `<head>` point at `https://postmillennium-mtb.github.io/headwaters-ledger/`. **Confirm that's the right GitHub Pages URL for this repo** — if the tool lives somewhere else, those two `og:url`/`og:image` lines are the only places the origin is written down. Without them a shared link unfurls as a bare URL with no title, description, or thumbnail.

## Sharing specific pages

Every region and the essay have their own link, using `#` at the end of the URL:

- `index.html#co` → Colorado
- `index.html#wy` → Wyoming
- `index.html#mt` → Montana
- `index.html#id` → Idaho
- `index.html#bc` → British Columbia
- `index.html#ab` → Alberta
- `index.html#essay` → the pipeline essay

Handy for linking straight to Colorado's 2026 countdown from an article, or straight to a region's Reservoirs tab (the link opens the region's page on the "Where It Goes" tab by default — mention the tab by name if you want someone to click over to Reservoirs once they land).

## A note on the numbers

Every specific figure in this tool — flow volumes, percentages, dates, dollar amounts, reservoir capacities — is marked one of two ways in the footer's "Data notes & confidence" section:

- **Solid**: comes directly from compact texts, government agencies, or court records.
- **Estimates (†)**: widely cited figures that vary by source, year, or measurement method — flagged with a dagger wherever they appear in the tool itself, not just the footer.

This matters especially for the pie charts on each region's page — those are proportions built from water plans and long-term averages, not a live gauge reading. It also applies to the **Reservoirs tab**: capacities and build years come from Wikipedia and individual dam or operator pages (Bureau of Reclamation, Army Corps of Engineers, state water agencies), checked in August 2026 — solid for the big numbers, but treat exact figures as approximate where multiple sources disagree (a few reservoirs, like Colorado's McPhee or Idaho's American Falls, have build-year ambiguity from later reconstructions, noted in their card text where it matters). Worth keeping all of this in mind if you ever present the tool in a room with a state water engineer in it.

## Ideas for what's next

A few directions this could grow, roughly in the order I'd tackle them:

1. **British Columbia and Alberta reservoir data** — still the most obvious next step. The pattern's proven on four states; it's a research-and-data-entry job now, not a design job. Adding entries to their `reservoirs:[]` arrays is the whole edit — both home-page cards pick them up on their own.
2. **A "compare all six" view.** Right now the only way to compare regions is to visit them one at a time and remember. Every number this would need — flow totals, retention shares, compact counts, reservoir ages — is already in `STATES`, so this is a rendering job, not a research job. It's the cheapest genuinely new *capability* on this list.
3. **Search / "find my river."** Type "Arkansas" or "Kansas" and land on the region that sends water there. The `rivers[]` array already holds every name and destination string; on a phone this would beat hunting for the right shape on the map.
4. **A tap-to-define glossary.** The tool says MAF, acre-foot, Lee Ferry, virgin water supply, and equitable apportionment without ever defining them. For a reader arriving from a Pinkbike article rather than a water-law background, that's the difference between "this is fascinating" and "this isn't for me."
5. **A Utah or New Mexico page** — both are Colorado River Compact signatories already referenced on Colorado's page, so they'd slot into the existing pattern easily. The map itself is the hard part (see the architecture notes above).
6. **More Water Series essays**, using the same card-on-the-map-page pattern as the pipeline essay. "What's an acre-foot, actually?" or "Who owns the rain that falls on your roof?" both feel like natural companions.
7. **A live reservoir gauge** for Lake Powell and Lake Mead on Colorado's countdown tab. Worth naming the tradeoff plainly: current storage levels are the numbers that most make the tool look alive, and also the ones that go stale fastest. Hand-updated, it becomes a standing chore and a credibility risk if you miss a few months. If you add it, put the reading's own as-of date right next to the number rather than relying on the footer.
8. **A "your household" calculator** — plug in your water bill or town, see your personal slice of the pie chart. This is the one that would take the tool from "explains the system" to "shows you where you personally sit in it," which is very on-brand for the rest of your tool suite.

None of these need to happen — the tool stands on its own as-is. Just flagging where the road keeps going, if you want it to.

---

*Built by Post Millennium Renaissance. Not legal advice — built by a trail advocate, not a water attorney.*
