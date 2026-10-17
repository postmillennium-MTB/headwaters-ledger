# PRD: Ledger Visual Identity — Six Themes and a Reordered Home Page

**Date:** 2026-10-16
**Feature:** 001-ledger-visual-identity

## Problem

The top of the Ledger's home page reads as a generic, AI-generated website: Palatino/Georgia serif, an italic gray intro paragraph with a bold call-to-action, a tracked uppercase monospace eyebrow over a heavy rule, a muted teal-and-rust palette on pale paper, and big-numeral stat tiles between hairlines. Together they give no sign of a particular author or subject. The intro paragraph and stats also push the search bar and map, the page's main interaction, well down a phone screen.

## Users & Context

Readers arriving from PMR articles or Pinkbike on phones, often inside an iframe, who want to know whether the water fight touches their state or river. The author (Jon) has no coding background and edits through GitHub's web UI. The Ledger is a single `index.html` with an existing four-theme picker driven by a `THEMES` registry and CSS palette blocks; its map and chart labels are width-fitted against a specific monospace stack and must not change.

## Goals

- Replace the four existing color themes with six: three directions in light and dark.
  - **A. Survey / map sheet:** Big Shoulders Display, Barlow Semi Condensed, IBM Plex Mono; benchmark-tile stats.
  - **B. Docket / court record:** Special Elite, Libre Caslon Text, Cutive Mono; "Finding 1/2" stat rows and a FILED stamp.
  - **C. Trailhead poster:** Alfa Slab One, Zilla Slab; framed layout and badge stats.
- Restyle the whole page (home, region pages, cards, controls) through the theme tokens so no screen keeps the old teal look.
- Move the intro paragraph, the two stats and the "See where it all ends up ↓" link from above the search bar to below the map (and its region list), directly above the continental chart. Wording unchanged.
- Embed all theme fonts in the file (ADR-001).

## Non-Goals

- No change to data, text wording, region pages' content, or chart logic.
- No change to the map and chart SVG label fonts or fitting constants.
- No new build step, no external requests.
- No "style" and "light/dark" as separate switches; each of the six is one theme in the existing picker.

## Success Criteria

- The picker shows six themes; each renders the home page with its own fonts and colors, with no leftover teal/rust from the old default.
- On a 390 px phone the search bar and map appear immediately under the title, and the intro, stats and jump link appear below the map.
- "See where it all ends up ↓" still scrolls to the continental chart.
- The stats still show live values from `continentalHeadline()`.
- Body text and stat labels meet WCAG AA contrast (4.5:1 for text, 3:1 for large text) in all six themes.
- The file works from a double-click offline, with all six themes showing their fonts.
- Existing smoke/verification checks still pass; the map and chart labels do not overflow in any theme.
- Saved theme preference migrates sensibly (a visitor with an old theme saved lands on a valid new default, not a blank or broken state).

## Architecture Decisions

- [Embed theme fonts as base64](../../adr/001-embed-theme-fonts.md) — keeps the single-file, works-offline promise; costs about 320 KB (+60%) in file size.

Decided inline, no ADR: replace the four themes with six (rather than add, or split style from light/dark) because a theme here is colors plus fonts plus decorative treatment, and six dots fit on a phone; reorder the home page as specified.

## Out of Scope

- Hand-tuning each theme's map and chart colors beyond what the tokens provide (revisit if any basin color fails contrast on a dark theme).
- A seventh theme, per-user font choice, or a print stylesheet.
- Applying the same identity to other PMR tools.
