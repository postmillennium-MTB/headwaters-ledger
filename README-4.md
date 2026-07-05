# The Headwaters Ledger

**A single-file interactive tool mapping where water goes from the six headwaters regions of the Rocky Mountains, and who controls it.**

Part of the Post Millennium Renaissance tool suite · `postmillenniumrenaissance.com`

---

## What this actually is

One HTML file (`headwaters-ledger.html`). No build step, no install, no dependencies. You open it in a browser and it works — which also means you can drop it straight into a GitHub Pages repo and iframe it into your site or a Pinkbike article, exactly like the other 13 PMR tools.

Everything — every state, every river, every quiz question — lives inside that one file as plain data. There's no database and nothing to configure. To change what the tool says, you (or a future Claude session) find the right paragraph of text inside the file and edit it directly.

## What's in it

**A clickable map** of six regions: Colorado, Wyoming, Montana, Idaho, British Columbia, and Alberta — the "headwaters club," the places where the continent's water is actually born. Click a region, get its own page.

**Each region's page has four tabs:**

| Tab | What it shows |
|---|---|
| Where It Goes | An interactive diagram of that region's rivers, which state/province/country each one flows to, and a pie chart of the split — plus which agreement governs each river |
| The Agreements | Every compact, treaty, or court decree that touches that region's water, filterable by "still in force forever" vs. "expiring or in limbo" |
| Countdown 2026 / The Stakes | Colorado gets a live countdown to the Colorado River rule changes; the other five get a "here's what's actually at risk" section |
| Quiz | 4–5 questions per region, multiple choice, with an explanation after each answer |

**One essay**, "Too Heavy, Too Cheap: Why America Pipes Oil and Not Water," reachable from a card on the map page. It answers a question people naturally ask once they've looked at the map: if we pipe oil across the country, why not water?

**Four color themes** (the dots in the top right): Snowmelt (default blue), Canyon (warm/orange), Nightflow (dark mode), Survey (sepia/vintage). These apply everywhere at once.

**A link back to your homepage**, top right, under the theme dots.

## How to update it (no coding required, but here's the shape of it)

Because this is one big file, "editing" really means: open the file, use Ctrl+F / Cmd+F to search for a phrase you want to change, and edit the text between the quote marks. A few landmarks to search for:

- To edit a fact or fix a typo in an existing region: search for a distinctive phrase from that sentence (e.g. search `"Kansas sued Colorado"` to jump straight to the Arkansas River entry).
- To add a new quiz question: search for `quiz:[` under the region you want, and copy the pattern of an existing question (the four-line block starting with `{q:`).
- To add a whole new region (a 7th state, say): that's a bigger job — it means adding a new data block plus a new shape on the map itself. Best done by describing what you want to Claude rather than hand-editing, since the map's shapes need to line up geometrically with each other.
- To add a new essay: same idea as the Too Heavy, Too Cheap essay — a block of content plus a card on the home page. Also best done with Claude's help the first time; after that, editing the *text* of an existing essay is just normal text editing.

**The safest way to make any change**, technical background or not: paste the file to Claude and describe what you want changed in plain English ("Colorado's second quiz question has a typo," "add a sentence to Wyoming's local box about X," "add a Utah page"). Claude can find the exact spot and make the edit without touching anything else — that's how every update to this tool has happened so far.

## Deployment

Same pattern as your other PMR tools:

1. Commit `headwaters-ledger.html` to the tool's GitHub repo (watch out for the known GitHub-web-UI issue where it sometimes creates a new branch instead of committing straight to `main` — double check before you navigate away).
2. GitHub Pages serves it automatically.
3. Iframe it into `postmillenniumrenaissance.com` or a Pinkbike article the way you do with the rest of the tools grid.

## Sharing specific pages

Every region and the essay have their own link, using `#` at the end of the URL:

- `headwaters-ledger.html#co` → Colorado
- `headwaters-ledger.html#wy` → Wyoming
- `headwaters-ledger.html#mt` → Montana
- `headwaters-ledger.html#id` → Idaho
- `headwaters-ledger.html#bc` → British Columbia
- `headwaters-ledger.html#ab` → Alberta
- `headwaters-ledger.html#essay` → the pipeline essay

Handy for linking straight to Colorado's 2026 countdown from an article, instead of making people click through the map first.

## A note on the numbers

Every specific figure in this tool — flow volumes, percentages, dates, dollar amounts — is marked one of two ways in the footer's "Data notes & confidence" section:

- **Solid**: comes directly from compact texts, government agencies, or court records.
- **Estimates (†)**: widely cited figures that vary by source, year, or measurement method — flagged with a dagger wherever they appear in the tool itself, not just the footer.

This matters especially for the pie charts on each region's page — those are proportions built from water plans and long-term averages, not a live gauge reading. Worth keeping that framing in mind if you ever present this in a room with a state water engineer in it.

## Ideas for what's next

A few directions this could grow, roughly in the order I'd tackle them:

1. **A Utah or New Mexico page** — both are Colorado River Compact signatories already referenced on Colorado's page, so they'd slot into the existing pattern easily.
2. **More Water Series essays**, using the same card-on-the-map-page pattern as the pipeline essay. "What's an acre-foot, actually?" or "Who owns the rain that falls on your roof?" both feel like natural companions.
3. **A live reservoir gauge** for Lake Powell and Lake Mead on Colorado's countdown tab, if you're willing to have it need occasional manual updates (or eventually pull from a public data feed).
4. **A "your household" calculator** — plug in your water bill or town, see your personal slice of the pie chart. This is the one that would take the tool from "explains the system" to "shows you where you personally sit in it," which is very on-brand for the rest of your tool suite.

None of these need to happen — the tool stands on its own as-is. Just flagging where the road keeps going, if you want it to.

---

*Built by Post Millennium Renaissance, 2026. Not legal advice — built by a trail advocate, not a water attorney.*
