# Feature 001: Ledger Visual Identity — Six Themes and a Reordered Home Page

**Status:** Approved
**Created:** 2026-10-16
**Branch:** `001-ledger-visual-identity`

---

## Problem Statement

The top of the Headwaters Ledger home page reads as a generic, templated website: a default serif body, an italic gray introduction with a bold call to action, a tracked uppercase monospace eyebrow over a heavy rule, a muted teal-and-rust palette, and large numerals between hairlines. Nothing signals a particular author or subject. The introduction and statistics also sit above the search bar and map, pushing the page's main interaction down the screen, especially on phones.

## Goals

- Replace the four existing color themes with six: three typographic directions (Survey, Docket, Poster), each in a light and a dark variant.
- Give every direction its own fonts, colors and decorative treatment, applied to the whole tool (home, region pages, cards, controls), not only the home page's top block.
- Move the introduction paragraph, the two headline statistics and the "See where it all ends up ↓" link from above the search bar to below the map (and its region list), directly above the continental chart, with wording unchanged.
- Bundle every font the six themes need inside the single `index.html` file, per ADR-001, so the file works offline and inside iframes with no outside requests.
- Keep every theme readable: normal text at least 4.5:1 contrast, large text at least 3:1.

## Non-Goals

- No change to data, to the wording of any existing text, or to region-page content.
- No change to the fonts, label fitting or sizing of the map and chart graphics.
- No separate "style" and "light/dark" switches: each of the six looks is one theme in the existing picker.
- No new build step and no network requests.

## Users and Context

**Primary users:** Readers arriving from Post Millennium Renaissance articles or Pinkbike, mostly on phones and often inside an embedded frame, who want to learn whether the Colorado River water fight touches their state or river.
**Secondary users:** The author, who edits the file through GitHub's web editor and has no coding background.
**Usage context:** A short first visit that starts with search or the map; some visitors return and pick a theme.
**User mental model:** The page is a ledger of who owns the water. They expect to find a search box and a map first, and an explanation after.

## User Stories

### Story 1: Search and map first

**As a** reader on a phone
**I want** the search bar and map directly under the title
**So that** I can start exploring without scrolling past text

**Acceptance criteria:**

- [ ] **AC-1.1** Given the home page is loaded at a 390 px viewport width When the page first renders Then the search bar appears immediately below the title and the map's top edge is visible without scrolling
- [ ] **AC-1.2** Given the home page is loaded at any viewport width, from 320 px to desktop When a reader scrolls down past the map and its region list Then the introduction paragraph, the two statistics and the "See where it all ends up ↓" link appear in that order, directly above the continental chart
- [ ] **AC-1.3** Given the home page is loaded When the introduction, statistics and link are read Then their wording is identical to the current wording, and the statistic values still come from the live data (85% and 2.1% today)
- [ ] **AC-1.4** Given a reader is on the home page When they activate "See where it all ends up ↓" Then the page scrolls to the continental chart

### Story 2: Pick one of six themes

**As a** reader
**I want** to choose from six distinct looks
**So that** I can read the Ledger in the style and brightness I prefer

**Acceptance criteria:**

- [ ] **AC-2.1** Given the home page is loaded When the theme picker is shown Then it contains exactly six choices named Survey Light, Survey Night, Docket Light, Docket Night, Poster Light and Poster Night, each readable by assistive technology, and none of the four former themes remains
- [ ] **AC-2.6** Given a first-time visitor with no saved choice When the page loads Then Survey Light is shown
- [ ] **AC-2.2** Given the picker is shown When a reader selects any theme Then the whole page, including the home page, a region page, cards and controls, switches to that theme's colors and fonts immediately with no reload
- [ ] **AC-2.3** Given a reader selected a theme When they reload the page or return later Then the same theme is shown
- [ ] **AC-2.4** Given a reader selects a dark theme When the page renders Then the browser's address-bar color and native controls match the theme's darkness
- [ ] **AC-2.5** Given each of the six themes is selected When the home page renders Then the title, introduction, statistics, search bar and buttons use that theme's defined fonts, and no element shows the former teal-and-rust styling

### Story 3: Distinct looks

**As a** reader
**I want** each direction to look clearly different from the others and from the old design
**So that** the Ledger feels authored, not templated

**Acceptance criteria:**

- [ ] **AC-3.1** Given the Survey themes are selected When the home page renders Then the title is set in tall condensed capitals, and the two statistics appear as bordered tiles labeled "BM"
- [ ] **AC-3.2** Given the Docket themes are selected When the home page renders Then the title is set in a typewriter face, a "FILED" stamp appears beside the eyebrow, and the statistics appear as ruled rows labeled "Finding 1" and "Finding 2"
- [ ] **AC-3.3** Given the Poster themes are selected When the home page renders Then the title is set in a heavy slab serif inside a double-ruled frame, and the statistics appear as filled badges
- [ ] **AC-3.4** Given the light and dark variant of the same direction When each is rendered Then they share fonts and layout and differ only in color

### Story 4: Works offline and embedded

**As a** reader opening the file from a double-click, or inside an embedded frame
**I want** every theme's fonts to appear without any network access
**So that** the Ledger looks the same everywhere

**Acceptance criteria:**

- [ ] **AC-4.1** Given the file is opened with no network connection When any of the six themes is selected Then that theme's fonts display, not substitute fonts
- [ ] **AC-4.2** Given the page is loaded When network activity is inspected Then no request is made to any font host or other outside address for fonts
- [ ] **AC-4.3** Given the page is embedded in a frame on another site When it loads Then all six themes display correctly

### Story 5: Readable in every theme

**As a** reader with low vision
**I want** adequate contrast in every theme
**So that** I can read the text, statistics and controls

**Acceptance criteria:**

- [ ] **AC-5.1** Given any of the six themes When the home page text (title, introduction, statistic labels, captions, search placeholder, buttons) is measured Then each normal-size text color has at least 4.5:1 contrast against its background and each large text at least 3:1
- [ ] **AC-5.2** Given a dark theme When the map, region list, continental chart and globe render Then every label and every basin color remains distinguishable against the dark background

### Story 6: Returning visitors keep a working theme

**As a** returning reader who previously chose an old theme
**I want** the page to still work
**So that** my saved choice doesn't leave a blank or broken page

**Acceptance criteria:**

- [ ] **AC-6.1** Given a reader's browser holds a saved theme that is one of the four former themes (Snowmelt, Canyon, Nightflow or the old Survey) When they open the page Then Survey Light is shown and the page renders fully
- [ ] **AC-6.2** Given a reader's browser holds an unrecognized saved theme value When they open the page Then Survey Light is shown and the page renders fully
- [ ] **AC-6.4** Given a reader's browser holds a saved choice that is one of the six new themes When they open the page Then that theme is shown
- [ ] **AC-6.3** Given the saved choice cannot be read or written (for example, storage is blocked) When the page loads Then Survey Light is shown and the picker still works for the visit

## Functional Requirements

### FR-1: Home page order

The home page shows, in this order: title, search bar, map with its region list, the map hint, introduction paragraph, headline statistics with the jump link, continental chart, then the remaining existing cards unchanged.

**Must:**
- Keep the introduction and statistics wording exactly as it is today
- Keep the statistic values computed from the live data

**Must not:**
- Duplicate the introduction or statistics elsewhere on the page
- Change region pages' own introductions

### FR-2: Six themes

The theme picker offers six themes: Survey light, Survey dark, Docket light, Docket dark, Poster light, Poster dark. Each theme defines the page's colors, its title and statistic font, its body font, its small-label font and its decorative treatment (per Story 3).

**Must:**
- Style the whole tool through the themes, including region pages, cards, tabs, forms and the globe's land and ocean colors
- Keep the map and chart basin colors fixed to their validated palette, adjusting only chrome around them

**Must not:**
- Retain any of the four former themes
- Change the fonts or sizing of text inside the map and chart graphics

### FR-3: Bundled fonts

Every font the six themes use is part of the single file (ADR-001), subset to the characters the Ledger needs, with each theme falling back to the existing system fonts if a bundled font fails.

**Must:**
- Name each bundled family, weight and license beside its data, in the file
- Make no outside request for fonts

**Must not:**
- Require any file other than `index.html` for the page to display correctly

### FR-4: Theme persistence and migration

The chosen theme is remembered between visits where the browser allows.

**Must:**
- Show Survey Light for any saved value that is not one of the six new themes, including the four former themes
- Keep honoring a saved choice of one of the six new themes
- Show Survey Light when the saved value is unreadable

## Non-Functional Requirements

### Performance

- The file size grows by no more than 350 KB over the current size (ADR-001 estimates about 320 KB).
- Switching themes completes with no visible delay and no flash of substitute fonts.
- Only the fonts used by the active theme are required to render the visible page.

### Security

- The page makes no new outside requests and sends no data anywhere.
- Saved theme values are validated before use.

### Reliability

- The page renders fully when storage is unavailable.
- The page renders at widths from 320 px to desktop with no horizontal scrolling and no overlapping text in any theme.
- Existing checks and tools (`tools/` scripts) continue to pass.

## Error Scenarios

| Scenario | Expected Behavior |
|----------|-------------------|
| A bundled font fails to decode | Text shows in the theme's fallback system font; the layout stays usable |
| Saved theme is an old or unknown value | Survey Light is shown, per AC-6.1 and AC-6.2 |
| Browser storage is blocked | Per AC-6.3 |
| The jump link's target is missing | The link does nothing and raises no visible error |
| Very narrow screen (320 px) with the longest title | The title wraps to a second line without clipping or overlapping |

## Open Questions

None. Resolved with the author on 2026-10-16:

- Default theme: Survey Light.
- Theme names: Survey Light, Survey Night, Docket Light, Docket Night, Poster Light, Poster Night.
- Saved themes: any saved value that is not one of the six new themes shows Survey Light (no per-theme mapping).
- Home page order applies at every width.
- "Tap a region to open its ledger" keeps its current wording, with no extra cue above the map.

## Out of Scope (Future Considerations)

- Hand-tuning the map and chart colors per theme beyond what the shared theme settings provide
- A seventh theme, per-reader font choice, or a print stylesheet
- Applying the same identity to other Post Millennium Renaissance tools
