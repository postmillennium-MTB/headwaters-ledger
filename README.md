# The Headwaters Ledger

**A single-file interactive tool mapping where water goes from the six headwaters regions of the Rocky Mountains, and who controls it.**

Part of the Post Millennium Renaissance tool suite · `postmillenniumrenaissance.com`

---

## What this actually is

One HTML file (`headwaters-ledger.html`). No build step, no install, no dependencies. You open it in a browser and it works — which also means you can drop it straight into a GitHub Pages repo and iframe it into your site or a Pinkbike article, exactly like the other PMR tools.

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
| Countdown 2026 / The Stakes | Colorado gets a live countdown to the Colorado River rule changes; the other five get a "here's what's actually at risk" section |
| Reservoirs | The region's major reservoirs — name, river, year built, capacity — with an average-age callout and combined-capacity stat. Populated for Colorado, Wyoming, Montana, and Idaho so far; British Columbia and Alberta show a "coming soon" card until that data's added |
| Quiz | 4–5 questions per region, multiple choice, with an explanation after each answer |

**One essay**, "Too Heavy, Too Cheap: Why America Pipes Oil and Not Water," reachable from a card on the map page. It answers a question people naturally ask once they've looked at the map: if we pipe oil across the country, why not water?

**Four color themes** (the dots in the top right): Snowmelt (default blue), Canyon (warm/orange), Nightflow (dark mode), Survey (sepia/vintage). These apply everywhere at once.

**A link back to your homepage**, top right, under the theme dots.

## How to update it (no coding required, but here's the shape of it)

Because this is one big file, "editing" really means: open the file, use Ctrl+F / Cmd+F to search for a phrase you want to change, and edit the text between the quote marks. A few landmarks to search for:

- To edit a fact or fix a typo in an existing region: search for a distinctive phrase from that sentence (e.g. search `"Kansas sued Colorado"` to jump straight to the Arkansas River entry).
- To add a new quiz question: search for `quiz:[` under the region you want, and copy the pattern of an existing question (the four-line block starting with `{q:`).
- **To add or edit a reservoir**: search for `reservoirs:[` under the region you want. Each entry is `{name, river, yearBuilt, capacityAF, note?}` — `note` is optional. British Columbia and Alberta currently have empty arrays (`reservoirs:[]`); populating those is the most obvious next step, and once you do, add their two-letter keys (`'bc'`, `'ab'`) to the `RESERVOIR_STATES` array near the top of the script so the home-page infrastructure-age card picks them up automatically — nothing else needs to change.
- To add a whole new region (a 7th state, say): that's a bigger job — it means adding a new data block plus a new shape on the map itself. Best done by describing what you want to Claude rather than hand-editing, since the map's shapes need to line up geometrically with each other, and the existing six already fill the available space tightly.
- To add a new essay: same idea as the Too Heavy, Too Cheap essay — a block of content plus a card on the home page. Also best done with Claude's help the first time; after that, editing the *text* of an existing essay is just normal text editing.

**The safest way to make any change**, technical background or not: paste the file to Claude and describe what you want changed in plain English ("Colorado's second quiz question has a typo," "add a sentence to Wyoming's local box about X," "add the BC reservoirs"). Claude can find the exact spot and make the edit without touching anything else — that's how every update to this tool has happened so far.

### For a future Claude session (architecture notes)

The file went through a maintainability pass and a couple of feature rounds after it was first built, so a few things are worth knowing before you dive in:

- **`TOOL_NUMBER`**, near the top of the script, is the single source for the "No. 14" catalog number shown in the eyebrow and on every region's ledger badge (`14-A` through `14-F`). Change it once there, not in the 14 places it used to be hard-typed.
- **`STATES`** is the one data object driving almost everything. There's a schema comment directly above it listing every field a region needs.
- **`THIRD_TAB`** is a small registry (`{crisis: {...}, stakes: {...}}`) that renders and wires up each region's third tab. Colorado uses `crisis` (the 2026 countdown); the other five use `stakes`. If you ever want a third kind of tab, add a new key here with `render(st)` and `wire(st)` functions — you won't need to touch `renderState()` itself.
- **`reservoirSummary()`** and **`barListHtml()`** are shared helpers — the first averages a region's reservoir data once so the per-region Reservoirs tab and the home-page infrastructure card can never disagree with each other; the second is a small reusable bar-chart renderer (built on the `.bars`/`.bartrack`/`.barfill` CSS already used by Colorado's countdown-math widget) used by both new home-page cards.
- **`escapeHtml()`** exists specifically for reservoir data pulled from outside sources (Wikipedia, dam-operator sites). The rest of the file's prose fields (`thesis`, `text`, etc.) intentionally contain hand-authored HTML like `<b>` and `<span class="flow">` for styling — don't wrap those in `escapeHtml()`, it'll break the formatting.
- The flow diagram (the "Where It Goes" SVG) uses a fixed-width layout on purpose — a narrower mobile version was tried and reverted because Wyoming's longest river name and Alberta's longest destination label start overlapping each other at smaller widths. If mobile legibility of that specific diagram ever needs to improve further, it'll need a real layout change (a stacked list below a breakpoint, most likely), not just resizing.

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

Handy for linking straight to Colorado's 2026 countdown from an article, or straight to a region's Reservoirs tab (the link opens the region's page on the "Where It Goes" tab by default — mention the tab by name if you want someone to click over to Reservoirs once they land).

## A note on the numbers

Every specific figure in this tool — flow volumes, percentages, dates, dollar amounts, reservoir capacities — is marked one of two ways in the footer's "Data notes & confidence" section:

- **Solid**: comes directly from compact texts, government agencies, or court records.
- **Estimates (†)**: widely cited figures that vary by source, year, or measurement method — flagged with a dagger wherever they appear in the tool itself, not just the footer.

This matters especially for the pie charts on each region's page — those are proportions built from water plans and long-term averages, not a live gauge reading. It also applies to the **Reservoirs tab**: capacities and build years come from Wikipedia and individual dam or operator pages (Bureau of Reclamation, Army Corps of Engineers, state water agencies), checked in August 2026 — solid for the big numbers, but treat exact figures as approximate where multiple sources disagree (a few reservoirs, like Colorado's McPhee or Idaho's American Falls, have build-year ambiguity from later reconstructions, noted in their card text where it matters). Worth keeping all of this in mind if you ever present the tool in a room with a state water engineer in it.

## Ideas for what's next

A few directions this could grow, roughly in the order I'd tackle them:

1. **British Columbia and Alberta reservoir data** — the most obvious next step. The pattern's proven on four states; it's a research-and-data-entry job now, not a design job. Once added, update `RESERVOIR_STATES` and both home-page cards pick it up automatically.
2. **A Utah or New Mexico page** — both are Colorado River Compact signatories already referenced on Colorado's page, so they'd slot into the existing pattern easily. The map itself is the hard part (see the architecture notes above).
3. **More Water Series essays**, using the same card-on-the-map-page pattern as the pipeline essay. "What's an acre-foot, actually?" or "Who owns the rain that falls on your roof?" both feel like natural companions.
4. **A live reservoir gauge** for Lake Powell and Lake Mead on Colorado's countdown tab, if you're willing to have it need occasional manual updates (or eventually pull from a public data feed). Distinct from the Reservoirs tab, which shows design capacity and age rather than current storage level.
5. **A "your household" calculator** — plug in your water bill or town, see your personal slice of the pie chart. This is the one that would take the tool from "explains the system" to "shows you where you personally sit in it," which is very on-brand for the rest of your tool suite.

None of these need to happen — the tool stands on its own as-is. Just flagging where the road keeps going, if you want it to.

---

*Built by Post Millennium Renaissance, 2026. Not legal advice — built by a trail advocate, not a water attorney.*
