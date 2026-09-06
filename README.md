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

- **"The West's Water Infrastructure Is Getting Old"** — a strip plot of every tracked reservoir's build year, computed live from each region's reservoir data (not typed in by hand — add or edit a reservoir and the chart and its peak-window band both update themselves).
- **"How Much Stays Home"**, sitting next to the essay card at half-width — a bar chart of what share of each region's annual flow is actually used there versus leaving for somewhere else, pulled directly from the same numbers already driving each region's flow chart.

**Each region's page has five tabs:**

| Tab | What it shows |
|---|---|
| Where It Goes | An interactive diagram of that region's rivers and which state/province/country each one flows to, plus a ribbon chart tracing every share of the region's flow to the ocean it finally reaches — and which agreement governs each river |
| The Agreements | Every compact, treaty, or court decree that touches that region's water, filterable by "still in force forever" vs. "expiring or in limbo" |
| Countdown 2026 / The Stakes | Colorado gets a live countdown to the Colorado River rule changes — which flips to counting the days *since* each deadline once it passes, so the tab never goes stale; the other five get a "here's what's actually at risk" section |
| Reservoirs | The region's major reservoirs — name, river, year built, capacity — with an average-age callout and combined-capacity stat. Populated for Colorado, Wyoming, Montana, and Idaho so far; British Columbia and Alberta show a "coming soon" card until that data's added |
| Quiz | 4–5 questions per region, multiple choice, with an explanation after each answer |

**A continental flow chart** on the home page — "Where It All Ends Up." Six regions on the left, every final destination on the right, ribbons sized by *actual annual volume* rather than by each region's own percentages. This is the one chart that says the thing all the others hide: about 85% of the water coming off the roof of the continent goes to just two places, the Pacific and the Arctic, while the Colorado — the river the entire 2026 fight is about — carries roughly 2% of it.

**A real map of the six regions** at the top of the page — accurate outlines, terrain, and the actual Continental Divide. Each region is a button that opens its ledger. It replaced six polygons tiling a fixed frame under a caption that read "Continental Divide (stylized, not geographic)". That caption was honest, and the map was diagrammatic rather than wrong, but it did two things worth fixing: it drew British Columbia at roughly Montana's size, when BC is 2.5× bigger by area and sheds about 4.4× the water (~200 MAF/yr against Montana's ~45); and it never showed the one fact the whole tool rests on, which is that these six regions are the high ground. Ground above 1,000 m, 2,000 m and 3,000 m is now shaded, so "the roof of the continent" is something you can see rather than a phrase the thesis asserts.

**A rotatable, zoomable globe**, directly under the continental chart. Same six regions, same destinations, same annual volumes — drawn on the earth instead of in a diagram. Drag it, spin it with the arrow keys, zoom in four stops with the buttons or `+`/`−`, double-click a place to bring it to the centre, or pick a region from the list underneath and it flies there and opens up far enough to read the names. Real coastlines (Natural Earth, embedded in the file, no CDN), a great-circle arc from each region to every ocean it drains to, thickness on the same volumes the ribbons use, colour on the same fixed basin palette.

It exists because the ribbon chart above it has no geography in it at all, and the claim underneath the numbers is geographic: five of the six regions sit within about 700 miles of each other on one mountain spine, and their water leaves for six different edges of the continent. That is a shape, and a Sankey cannot draw it. The region pins are not political centroids — each sits on that region's hydrological high ground, so Montana's is Triple Divide Peak and Alberta's is Snow Dome on the Columbia Icefield.

**A search box** above the map. Type a river ("Snake"), the state you live in ("Kansas" finds the Arkansas River, because the index knows KS is Kansas), a compact year ("1922"), a reservoir ("Blue Mesa"), or a term ("acre-foot"), and the result takes you straight to the right region *and the right tab*. Enter picks the top hit.

**Rivers colored by where they end up.** Every river in the "Where It Goes" diagram is drawn in its destination basin's color, so a blue line means the Pacific whether you're looking at Idaho's rivers, Colorado's ledger, or the whole continent — one visual language across the tool. Montana's diagram makes its three-oceans claim visible at a glance: two blue lines, three green. A faint dashed current drifts downstream along each river (purely decorative, and switched off entirely for anyone who has reduced motion turned on).

**A reservoir build-year strip plot** on the home page, replacing the old average-age bars. Every dot is one reservoir, placed on the year it was built. The average was the *summary* of the story; the strip plot **is** the story — you can see that 17 of the 21 reservoirs went in between 1939 and 1969. That window is computed from the data, not typed in, so it moves if BC and Alberta are ever added.

**Ribbon flow charts** on every region page, replacing the old donut. A donut answers "what share?" and buries the destination in a sub-label; the entire subject of this tool is water *arriving somewhere else*, so the chart now draws share and destination in a single mark. Hover or tap any ribbon, bar segment or legend row and all three light up together.

**A compare view** — all six regions in one sortable table: annual flow, how much stays home, rivers tracked, agreements signed and how many are expiring, reservoir count and average age. On a phone the table becomes stacked cards with their own sort control. Every column is computed from the region data, so nothing here can drift out of step with the individual pages.

**A household calculator** — set your household size and gallons per person per day, pick a region, and see your own water use in acre-feet, how many households share one acre-foot, and how your house compares to the gap between what the 1922 Compact promised and what the river actually carries. It exists because every other number in the tool is in millions of acre-feet, which nobody has an intuition for.

**A glossary** of thirteen terms — acre-foot, MAF, Lee Ferry, virgin water supply, prior appropriation, equitable apportionment, and the rest. These are tappable *wherever they appear anywhere in the tool*: the first time a defined term shows up in any paragraph it becomes a dotted link, and tapping it slides a definition up from the bottom of the screen. Add a term to the registry and it starts linking itself everywhere; there is no list of "which words are linked" to maintain.

**One essay**, "Too Heavy, Too Cheap: Why America Pipes Oil and Not Water," reachable from a card on the map page. It answers a question people naturally ask once they've looked at the map: if we pipe oil across the country, why not water?

**Four color themes** (the dots in the top right): Snowmelt (default blue), Canyon (warm/orange), Nightflow (dark mode), Survey (sepia/vintage). These apply everywhere at once, and your choice is remembered between visits.

**A link back to your homepage**, top right, under the theme dots.

**On a phone**, five things change shape rather than just shrinking. The ribbon charts become full-width proportional bars carrying the same numbers, the same basin colors and the same tap-to-highlight — the Sankey's geometry is its whole value and it does not survive being squeezed to 330px. The map gains a tappable list of the six regions underneath it, each with the one-line résumé that desktop readers only get by hovering. And each region's river diagram is replaced by a stacked list of the same rivers at readable size — the diagram itself is drawn at a fixed width, so at phone scale its labels came out around four pixels tall. The reservoir strip plot gets its own narrower frame rather than being scaled down, for the same reason. And the globe drops its ocean labels rather than shrinking them — its type is a fixed 11px at every canvas size, so the only thing a narrower frame can give up is how many strings compete for the margin; the list under it names every destination in full either way. Everything else (back button, browser back gesture, quiz retry, tapping a ribbon and tapping it again to clear) is sized and wired for thumbs.

## How to update it (no coding required, but here's the shape of it)

Because this is one big file, "editing" really means: open the file, use Ctrl+F / Cmd+F to search for a phrase you want to change, and edit the text between the quote marks. A few landmarks to search for:

- To edit a fact or fix a typo in an existing region: search for a distinctive phrase from that sentence (e.g. search `"Kansas sued Colorado"` to jump straight to the Arkansas River entry).
- To add a new quiz question: search for `quiz:[` under the region you want, and copy the pattern of an existing question (the four-line block starting with `{q:`).
- To move a pin on the globe, or point a region at a destination it doesn't yet reach: search for `GLOBE_REGION_PIN` (the six regions' lat/lon) or `GLOBE_SEA_PIN` (the river mouths). Adding a destination pin is the whole edit — its arc appears on its own. The two destinations with no pin (`home`, water used where it falls, and `mixed`, Wyoming's three-way split) are deliberate: neither has anywhere to draw *to*, and both are still listed in full, marked "no arc", in the text key under the globe.
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
- **`GLOSSARY`** is the term registry, and `linkTerms()` is the thing to understand before touching it. It walks **text nodes only**, which is the entire safety argument for auto-linking prose that contains hand-authored HTML — it is structurally incapable of inserting a button inside a tag or splitting an element. It links each term at most once per render, skips anything already interactive (a term inside a quiz answer would swallow that answer's click), and skips SVG, whose `<text>` elements cannot hold HTML children. Matching is literal and whole-word, so a term written with markup inside it (`acre-<b>foot</b>`) will not be found — keep defined terms unstyled in the prose.
- **`BASINS` and `SEAS`** drive the flow charts. Every pie slice carries a `sea` (where that water actually ends up); every sea belongs to a `basin`, and **the basin is what carries color**. That split is load-bearing, and the reason is measured rather than aesthetic: six mutually distinguishable categorical hues do not exist — no six-hue set clears the colorblind-separation and normal-vision floors on both the light and the dark theme surface. Four does. So hue groups destinations into four ocean basins, and the exact destination is carried by the directly-labeled node every ribbon lands on, plus a text chip on every legend row. Nothing depends on color alone, which is what makes the four-hue set legal at its measured separation. The hexes are **fixed across all four themes** — they mean something, and PMR's rule is that meaning-carrying color doesn't follow the theme. If you change one, re-run the dataviz validator against all four theme surfaces; do not eyeball it.
- **`reservoirStripSvg()`** and **`peakBuildWindow()`** draw the build-year plot. The shaded band is the 30-year span containing the most reservoirs in the whole set, found by search rather than hard-coded.
- **`MONO_ADVANCE`** is 0.723 — the width of one monospace character as a fraction of font size, **measured off the rendered SVG, not guessed**. A first attempt used 0.6 and still overflowed. Every SVG text-fitting calculation in the file derives from it.
- **`sankeySvg()`** is one renderer serving both flow charts (a region's outflow, and the six-region continental view) because they are the same shape with different inputs. Two things in it exist because of real bugs: the frame is **sized from the longest label string**, since SVG clips silently when text runs past the viewBox; and `deCollide()` pushes overlapping labels apart, because node height is proportional to volume and the real data spans three orders of magnitude — the Great Salt Lake's bar is a hairline while its label is still 13px tall, so centring every label on its own node stacks four of them on top of each other.
- **The globe is a `<canvas>`, and that is a measured decision rather than a stylistic one.** The coastline set is ~5,800 densified points that get re-projected on every animation frame; 5,800 live SVG nodes re-attributed 60 times a second is not something a phone will do. Canvas also sidesteps the scaling trap that bit `flowSvg()`: the backing store is sized in *device* pixels and every mark is drawn in *CSS* pixels, so a 262px phone globe and a 480px desktop globe draw their labels at the same 11px. Nothing scales with the container, so nothing shrinks below legibility.

  **What canvas costs is accessibility**, and that is paid for explicitly rather than waved at. A `<canvas>` is one opaque node to a screen reader and unreachable by keyboard, so the card carries the same information twice: the picture, and `.globe-key` — six real focusable buttons, one per region, each carrying that region's coordinates and every destination it reaches with the volume in millions of acre-feet. Clicking one spins the globe to it and highlights its arcs. **Delete the key and the card becomes mouse-only.** The canvas itself is focusable and takes the arrow keys as well.

- **`topoDecode()` and the negative-index trap.** In TopoJSON, an arc index of `-1` inside a ring does *not* mean "arc -1" — it means "arc 0, walked backwards" (`-2` is arc 1 backwards, and so on; the encoding is ones-complement, so the arc you want is `~i`). Get that sign wrong and the map still draws: continents land in roughly the right places and coastlines still look like coastlines, but every ring built from a reversed arc is wound inside out, so the fill swaps land and sea along that coast. It throws nothing and it is not obvious at a glance — the only reliable check is to look at several rotations. `land-110m.json` happens to contain no negative indices at all, so the branch is unexercised as shipped; it is written correctly anyway because `land-50m` and `countries-110m` both use them.

- **Back-face culling, and why the land fill is not just "skip the hidden points."** An orthographic projection maps *both* hemispheres onto the same disc, so without a visibility test the far side draws straight through the near side. Testing each point is easy; closing a *filled* polygon that runs off the edge of the visible hemisphere is the actual work. What `globeLandPath()` does: every hidden vertex is pushed radially out onto the horizon circle, and any two consecutive points that both sit on that circle are joined *along* it rather than across it. Because orthographic is one-to-one on the visible hemisphere, that reproduces the true clipped outline exactly. Two failure modes it has to dodge, both of which look plausible rather than broken — a ring with no visible vertex at all would collapse onto the rim and fill a crescent of ocean (those rings are skipped outright), and two rim points joined by a straight line cut a chord across the middle of the globe (the join walks the circle in small steps instead).

- **`LAND_110M` is the one piece of data in the file nobody may hand-edit.** Natural Earth 1:110m land polygons, quantized TopoJSON, verbatim from the npm package `world-atlas@2` (ISC packaging of public-domain data), embedded rather than fetched because the tool has to work from a `file://` double-click and inside a cross-origin iframe. Every number in it is a *delta* from the one before it, so changing any single value silently shifts every point after it. To change resolution, replace the whole string with `land-50m.json` from the same package and change nothing else — `topoDecode()` reads the quantization transform out of the data. Be aware that costs ten times the bytes: this one addition took the file from 257KB to 359KB, which matters mainly because the GitHub web editor gets sluggish at that size.

- **The globe labels regions with two-letter codes, not names, and the card's own headline is what forces it.** Five of the six pins sit inside about 700 miles of each other — that proximity *is* the claim — so on a 480px globe the whole cluster is roughly 100px across, and "British Columbia" alone is 218px of monospace. Six names cannot be attached to six pins in that space by any placement rule; they can only be fanned out on leaders until nobody can tell which name belongs to which dot. Codes fit, and no name is lost: the key spells out all six, and hovering or focusing a key row prints that region's full name on the globe. Note that none of this needs `MONO_ADVANCE` — canvas has `measureText()`, so the estimate that constant exists to supply for SVG is available here as a fact, per label, at the weight it is actually drawn in.

- **The globe is limb-shaded, in neutral rather than in theme colours.** A sphere lit from anywhere is darker at its edge than at its centre, and without that an orthographic projection is a circle with a line around it. Two radial passes: a darkening toward the limb, and a soft off-centre highlight that gives the light a direction. They are black and white at low alpha on purpose — this is a *lighting* model, not a palette. On Nightflow the theme's ink is nearly white, so darkening the limb with it would make the edge glow; neutral works on all four surfaces because "away from the light" means the same thing on every one of them.

  **It is drawn after the land and before the arcs**, which is the whole reason it's safe. The arcs carry meaning in the fixed basin palette, and dimming them 20% at the limb would shift a colour a reader is being asked to match against a key. So the shading falls on the ground and the water stays untouched — the same split the map makes between terrain and rivers.

- **The globe's zoom is a four-stop ladder, not a free multiplier, and where it stops is the design decision.** `GLOBE_ZOOM_STOPS = [1, 1.6, 2.4, 3.6]`. A ladder can't strand a reader on a half-useful magnification, every stop can be checked by eye, and the ceiling becomes an explicit statement rather than an emergent one. It stops at 3.6× for two independent reasons, both checked at each stop rather than derived: **the data** — Natural Earth 1:110m carries a vertex every ~33–355 km, sub-pixel at 1× and about 2px at 3.6×, but 3–6px by 5×, where Vancouver Island is visibly a polygon; and **the composition** — past ~3.6× the frame holds the six pins and almost nothing else, no coastline, no landmark, arcs floating on blank fill, which reads as a bug rather than a close-up. Going deeper means adding stops *and* swapping `LAND_110M` for land-50m. One without the other is a regression whichever you do first.

  **2.4× is where the card is at its best**, which is why picking a region flies to exactly that stop: all six regions named and separated, all six destinations named, every arc traceable with its thickness legible, and the continent still recognisable underneath. At 1× the six pins are a knot, so "take me to Alberta" that left the view at 1× wouldn't have taken anyone anywhere.

- **Zoom is on buttons, keys and double-click — not on the wheel or on pinch, and that's the same refusal as `pan-y`.** A bare `wheel` handler on a card inside an article iframe swallows the page scroll; a two-finger pinch is how a phone reader magnifies the *page*, which is an assistive behaviour and not ours to take. So: `+`/`−` buttons (40px targets right under the globe), `+`/`−` keys when the canvas has focus, and double-click to bring a place to the centre and step in — which wraps back to 1× at the top stop, because a zoom control with no exit strands people over oceans. Ctrl/⌘+wheel is the one wheel path, and it gives desktop trackpad pinch for free since that arrives as a `ctrlKey` wheel event.

- **Region labels are codes at 1× and names from 2× up** (`GLOBE_NAMES_AT_ZOOM`). The codes exist only because the cluster is ~100px wide at 1×; zoom spreads it and the constraint lifts. Nothing is forced — `globePlaceLabels` still drops whatever won't fit, and the key always carries all six in full. Note `GLOBE_LABEL_PAD_X` is wider than the vertical spacing on purpose: two labels sharing a baseline four pixels apart read as one run-on string ("MontanaWyoming") where two stacked at the same gap are unambiguous.

- **The land fill culls on bbox intersection, never on "are any vertices on screen."** Zoomed in, most of the world is off-canvas and re-pathing it every frame is waste — but zoomed deep inside Eurasia, every one of its vertices is off-canvas while its fill covers the entire frame. A vertex test would erase the ground under the reader's feet.

- **The map pans and zooms by moving its viewBox, which is the whole trick.** An SVG viewBox *is* a camera, so zooming is one attribute write, nothing is re-projected, and the vectors stay crisp at every stop. What it does not give you free is constant-size marks — SVG scales its contents with the viewBox — so every stroke width and font size on the map is written as `calc(Npx * var(--map-k))`, and `wireMap()` keeps `--map-k` equal to `viewWidth/900`. Forget it and zooming in gives you a four-pixel Continental Divide and labels the size of a state.

  Zoom is a four-stop ladder (`MAP_ZOOM_STOPS`), opening at 610 units — about 1.5×. **That default holds all four US regions whole, Alberta's southern half across its full width, and British Columbia's southeast including both river mouths that matter, the Fraser at Vancouver and the Columbia.** What falls outside is the northern halves of BC and Alberta and BC's outer coast. That trade only goes one way: a view tight enough to make the US states large cannot also hold BC's Pacific coastline, because they are 600 miles apart. One stop out restores everything, which is why the zoom-out control sits *on* the map rather than under it. `MAP_HOME_IX = 0` opens on the whole picture instead.

- **Labels are re-emitted on every view change, and de-collided.** A map label has to sit over the thing it names *and* inside the frame, which a fixed x/y cannot do once the camera moves — so each name is clamped into the overlap of its region's outline and the current view. That alone is not enough: crop to the US states and BC and Alberta are both reduced to a strip along the top edge, where clamping them independently renders "BRITISH COLUMALBERTA". The blocks are de-collided, and a block with no clear slot inside its own region is dropped rather than stacked. The search tries 16 slots, not 8 — a region clipped at the top has its whole outline above the frame, so half the candidates are unreachable and eight of them gave up while 150 units of British Columbia sat empty below.

- **A drag that moved the map must not also navigate.** `mapSuppressClick` is set by a pan and read once by the region click handler. Without it, dragging across Colorado opens Colorado when you let go.

- **Touch panning is deliberately not wired.** Inside an article iframe a one-finger drag has to stay page scroll, and the two-finger alternative is a decision that has not been taken. Until it is, `touch-action` is left alone so the page scrolls normally over the map, and touch readers get the default view, the zoom buttons and the region list — all of which work.

- **The home map is baked at build time, not projected at runtime.** `MAP_GEO` holds SVG path data already in viewBox units — Albers equal-area conic, standard parallels 43°N/55°N, clipped and simplified in screen units and rounded to a tenth of a unit. A map that never pans or zooms has no reason to pay for trigonometry, so the only thing projected at runtime is single points, via `mapProject()`. **Equal-area is the load-bearing choice**: the tiled map equalised BC and Montana, which is the same flattening the per-region pies make and that the continental card exists to correct.

- **The Continental Divide on that map is survey data, not a drawn line.** It is the shared boundary of the Pacific-draining and Atlantic-draining HUC2 regions of the USGS Watershed Boundary Dataset, joined to the British Columbia/Alberta provincial boundary — which *is* the Divide from the 49th parallel to about 54°N, and from there north is the 120th meridian, a survey line and not a watershed, so that stretch is cut off. One continuous line from the Mexican border into Canada. Two traps are recorded in `tools/build-map-data.py`: an exact boundary intersection **shatters** wherever two polygons' vertices don't coincide (through Montana it turned one 6° divide into eleven sub-half-degree crumbs that a length filter then silently discarded, leaving a plausible-looking divide with a hole in it) — matching within a tolerance is the robust question; and Albers `y` counts north while SVG `y` counts down, which renders the whole map upside down if you forget it.

- **What is deliberately NOT on that map: the Northern (Hudson Bay) Divide.** WBD is a US dataset, so the only available part is the Souris-Red stretch out in the Dakotas — the half that matters here, running west from Triple Divide Peak, lies in Canada where no comparable data is reachable (HydroSHEDS is not, and Natural Earth has no basins). Half a divide drawn as though it were whole is exactly the kind of quiet lie the data rules exist to stop. Triple Divide Peak is a marked point instead.

- **`tools/build-map-data.py` is not part of the page.** `index.html` never loads it and the tool still runs from a double-click with no build step. It exists because `MAP_GEO` is 45 KB of machine output that nobody can hand-edit, and data like that needs a way to be made again. Its Albers parameters are duplicated in `index.html` (`MAP_ALBERS`) on purpose — the page projects the headwaters pins at runtime from the lat/lon already in its data block rather than storing a second copy of them in viewBox units. Change a parameter in one place and you must change it in the other, or the pins land somewhere plausible and wrong.

- **The map has its own mobile frame, and bigger type was the wrong answer.** Scaled to a 340px phone, a 900-unit viewBox renders 23px labels at about 9 CSS px — but inflating them to 33px puts "BRITISH COLUMBIA" across 416 of the 900 units and on top of Alberta. So below 700px the map carries two-letter codes and nothing else, and the pick-list underneath carries all six names and résumés at real body size. Both label sets are always in the DOM and CSS picks one, the same arrangement `flowSvg()`/`flowList()` use, so the two can never name different regions.

- **`touch-action: pan-y` on the globe canvas, deliberately not `none`.** A reader flicking down the page has to keep scrolling even when their thumb lands on the globe, so vertical gestures stay the browser's; a horizontal one starts a rotation and captures the pointer, after which both axes follow the finger. The axis the browser keeps is still reachable another way — the arrow keys, and every region button. `touch-action:none` would make the globe drag beautifully and trap anyone trying to scroll past it.

- **The globe's page-level listeners are bound once for the life of the document**, dispatching through two module-level hooks. The router rebuilds the home page — and therefore this card — every time a reader comes back from a region page, so a `visibilitychange` listener added per wiring would accumulate one per visit, each pinning a retired canvas and its buffers in memory. The animation also stops whenever the card scrolls out of view or the tab goes to the background; a globe spinning below the fold burns a phone's battery to animate nothing.

- **The globe's three colors are the one theming exception in reverse.** `--globe-ocean`, `--globe-land` and `--globe-coast` live in each theme's CSS block alongside the rest of that palette, because they are *chrome* — unlike the basin hexes they follow the theme. A new theme's block has to carry them or the globe falls back to Snowmelt's three, which on a dark theme looks wrong rather than breaking. And because the globe is pixels rather than CSS-painted marks, `applyTheme()` has to *tell* it to redraw; that is what `globeRepaint` is for.

- **Sentences that expire carry their own replacement.** This tool's subject is paperwork with expiry dates on it, which means its prose has expiry dates on it too. On 1 January 2027 a reader would have found a page still saying the operating rules "expire in 2026", and a quiz still saying Reclamation "is finalizing" guidelines that took effect the previous October — a stale claim inside a quiz *answer* being the worst kind, since the reader is told they are right or wrong by a sentence that is neither.

  The countdown tab already solved this with paired `cap`/`capAfter` fields, but that only works where one renderer owns the string. These five sentences live in five different fields read by five different renderers (a thesis, a river's text, `compactsSub`, a compact's text, a quiz answer), so the pairing moved into the prose instead:

  ```
  {{YYYY-MM-DD|text before that date|text from that date on}}
  ```

  `resolveTense()` resolves them once at load, in place, before anything renders — the authored content stays in the data block where content belongs, and the logic is one function. A malformed marker fails to match and renders literally, which is loud and findable: the deliberate opposite of a tense that quietly goes wrong four months after anyone last looked.

- **Three status claims are still on a human, not a date.** "another from 1964 currently in limbo", "remain paused", "currently on pause" — all Columbia River Treaty status, in Montana's, Idaho's and BC's entries. No date will fix these; they go stale whenever negotiations move and nothing in the tool will notice. `LAST_REVIEWED` is the current answer, but a footer stamp doesn't attach to a specific sentence, so a reader has no way to know *that claim* is the one riding on it. Worth a per-claim `checked:` date someday; the underlying facts need sourcing either way.

- **`CMP_COLS`** is the compare table's column registry: label, sort field, and cell formatter. One entry adds a column to the desktop table, the mobile cards, and the mobile sort dropdown at once.
- **`ROUTE_VIEWS`** is the router's registry of standalone views (`essay`, `compare`, `glossary`, `household`). Adding one is a line here plus its render function.
- **`buildSearchIndex()`** builds the search index from `STATES` on first use. Each entry records the region *and* tab it lives on, which is why results can deep-link. `PLACE_NAMES` widens destination strings so searching "Kansas" matches a river whose destination reads "KS".
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
- `index.html#compare` → the six-region comparison
- `index.html#household` → the household calculator
- `index.html#glossary` → the glossary

A region link can also name a tab, which is what the search results use:

- `index.html#co/reservoirs` → Colorado, opened on its Reservoirs tab
- `index.html#wy/compacts` → Wyoming, opened on The Agreements
- Tab ids are `flow`, `compacts`, `third`, `reservoirs`, `quiz`. An unrecognised one just opens the region's first tab rather than erroring.

Handy for linking straight to Colorado's 2026 countdown from an article, or straight to a region's Reservoirs tab (the link opens the region's page on the "Where It Goes" tab by default — mention the tab by name if you want someone to click over to Reservoirs once they land).

## A note on the numbers

Every specific figure in this tool — flow volumes, percentages, dates, dollar amounts, reservoir capacities — is marked one of two ways in the footer's "Data notes & confidence" section:

- **Solid**: comes directly from compact texts, government agencies, or court records.
- **Estimates (†)**: widely cited figures that vary by source, year, or measurement method — flagged with a dagger wherever they appear in the tool itself, not just the footer.

This matters especially for the flow charts on each region's page — those are proportions built from water plans and long-term averages, not a live gauge reading. It also applies to the **Reservoirs tab**: capacities and build years come from Wikipedia and individual dam or operator pages (Bureau of Reclamation, Army Corps of Engineers, state water agencies), checked in August 2026 — solid for the big numbers, but treat exact figures as approximate where multiple sources disagree (a few reservoirs, like Colorado's McPhee or Idaho's American Falls, have build-year ambiguity from later reconstructions, noted in their card text where it matters). Worth keeping all of this in mind if you ever present the tool in a room with a state water engineer in it.

## Ideas for what's next

A few directions this could grow, roughly in the order I'd tackle them:

1. **British Columbia and Alberta reservoir data** — now the only thing standing between the Ledger and a complete storage picture, and the one item on the old list that is *blocked on facts rather than on code*. Everything downstream is already built and waiting: adding entries to those two `reservoirs:[]` arrays is the whole edit, and the Reservoirs tabs, the infrastructure-age card, and the compare table's "not yet added" rows all fill in on their own.

   What it needs is real sourcing, not a plausible guess. Three traps to avoid whenever this gets done:
   - **Units.** Canadian sources quote reservoir volume in cubic kilometres, cubic decametres or megalitres, never acre-feet. One acre-foot is 1,233.48 m³. Convert deliberately and write the converted number in, since `capacityAF` is what every calculation reads.
   - **Which volume.** "Gross capacity", "live/active storage" and "water volume" are three different numbers for the same reservoir, and they can differ by half. The four U.S. states in here are entered as design/gross capacity — match that, or the combined-capacity stat compares unlike things.
   - **Which year.** The average-age card is driven entirely by `yearBuilt`, so a wrong year quietly corrupts a chart on the home page. Dam completion, first impoundment, and full-pool dates are often years apart, and several of these dams were raised or rebuilt later.

   The obvious candidates: **BC** — Williston Lake (W.A.C. Bennett Dam, Peace), Kinbasket Lake (Mica), Arrow Lakes (Hugh Keenleyside), Lake Revelstoke, Duncan Lake. **Alberta** — Abraham Lake (Bighorn Dam), Oldman Reservoir, Lake Newell, Gleniffer Lake (Dickson Dam), St. Mary Reservoir. Best sources are BC Hydro's own dam pages and Alberta Environment and Protected Areas, with Wikipedia only as a cross-check.
2. **A Utah or New Mexico page** — both are Colorado River Compact signatories already referenced on Colorado's page, so the *data* slots into the existing pattern. **The map is no longer the blocker.** It used to be: six polygons tiled a fixed 660×800 viewBox with no room left, so a seventh region meant redrawing the whole arrangement. Now that the map is real geography, Utah and New Mexico are simply there — adding one is an entry in `STATES`, a lat/lon in `GLOBE_REGION_PIN`, a line in `MAP_TAGS`, and a re-run of `tools/build-map-data.py` with the new name in its `SIX` list. What's left is the research, which is the part that should have been the hard part all along.
3. **More Water Series essays**, using the same card-on-the-map-page pattern as the pipeline essay. "What's an acre-foot, actually?" or "Who owns the rain that falls on your roof?" both feel like natural companions — and the glossary now covers enough of the vocabulary that an essay could lean on it instead of stopping to define things.
4. **A live reservoir gauge** for Lake Powell and Lake Mead on Colorado's countdown tab. The tradeoff, plainly: current storage levels are the numbers that most make the tool look alive, and also the ones that go stale fastest. Hand-updated it becomes a standing chore and a credibility risk if you miss a few months — worse than not having it, because a confidently wrong current number undermines the figures around it that *are* right. If you add it, put the reading's own as-of date beside the number rather than relying on the footer stamp, and source it from Reclamation's public data rather than a news article.

None of these need to happen — the tool stands on its own as-is. Just flagging where the road keeps going, if you want it to.

---

*Built by Post Millennium Renaissance. Not legal advice — built by a trail advocate, not a water attorney.*
