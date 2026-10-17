# ADR-001-embed-theme-fonts: Embed theme fonts as base64 inside index.html

**Status:** Accepted
**Date:** 2026-10-16
**Feature:** 001-ledger-visual-identity

## Context

The Ledger is a single-file, zero-dependency tool with no web fonts: it uses system stacks (Palatino/Georgia body, system mono). The new visual identity (see the PRD) replaces the four color themes with six, in three typographic directions (Survey, Docket, Poster). Each direction needs fonts with no system equivalent: Big Shoulders Display, Barlow Semi Condensed, IBM Plex Mono (Survey); Special Elite, Cutive Mono, Libre Caslon Text (Docket); Alfa Slab One, Zilla Slab (Poster). Twelve font files in all (8 families, two weights for four of them).

Constraints: the file must work when double-clicked (no network), must work when iframed on postmillenniumrenaissance.com and in Pinkbike, and is edited by a non-coder through GitHub's web UI. Measured Latin-subset sizes: 287 KB woff2 as served by Google Fonts; 241 KB after trimming to Basic Latin, Latin-1, common punctuation and arrows; about 321 KB once base64-encoded. `index.html` is currently 537 KB.

## Options Considered

### Option A: One Google Fonts `<link>` for all eight families

**Pros:** Smallest edit; matches the MTB Patent Atlas; fonts cached across PMR tools.
**Cons:** Adds an external dependency and a network round-trip; fails offline and in locked-down embeds; every visitor downloads fonts for themes they never use; breaks the file's "zero-dependency" promise.

### Option B: Load only the active theme's fonts from Google Fonts on demand

**Pros:** Visitor downloads only what they see; system fonts remain the fallback.
**Cons:** Still an external dependency and still fails offline; more script to maintain; a flash of fallback type on every theme switch.

### Option C: Embed the fonts as base64 `@font-face` data URIs in the file

**Pros:** Keeps the file self-contained and working from a double-click, offline, and in any iframe; no third-party request or privacy exposure; no flash of unstyled type; browsers decode a data-URI font only when a rule using it is applied, so a visitor decodes only the active theme's fonts.
**Cons:** Adds about 320 KB (+60%) to a 537 KB file that every visitor downloads once, including fonts for themes they never open; the base64 blocks are not hand-editable and make the file harder to scan; changing a font means regenerating its block; the font licenses must be honored in the file.

## Decision

**We chose Option C** because the Ledger's core promise is a single file that works anywhere, including offline and inside third-party iframes, and Options A and B both give that up. The size cost is accepted as the price of that promise.

Implementation notes for the plan: the base64 blocks live together in one clearly labeled section of the `<style>` block, outside the design tokens, with a comment naming each family, weight, license and source URL. Fonts are subset to Basic Latin, Latin-1, and the punctuation and arrow glyphs the file uses. Each theme's font stack ends in the existing system fonts as a fallback. Font license texts are verified before shipping (the families are believed to be SIL OFL or Apache 2.0, both of which permit embedding; confirm against fonts.google.com for each family).

## Consequences

Easier: offline use, privacy, consistent rendering, no layout shift from late-loading fonts.

Harder: the file grows to roughly 860 KB; adding a seventh theme with new fonts adds another 40-90 KB; editing fonts needs the subsetting step (documented in `tools/`). If load weight on phones becomes a problem, revisit by (1) trimming display-only fonts to ASCII, (2) dropping weights, or (3) superseding this ADR with Option B.
