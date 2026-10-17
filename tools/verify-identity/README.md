# Identity checks

Headless-browser checks for `docs/specs/001-ledger-visual-identity`. Dev-only; nothing here is loaded by `index.html`.

```
NODE_PATH=<folder containing playwright> node tools/verify-identity/themes.js
NODE_PATH=<folder containing playwright> node tools/verify-identity/treatments.js
NODE_PATH=<folder containing playwright> node tools/verify-identity/order.js
```

Each prints one `ok` / `FAIL` line per check and exits non-zero on any failure. Set `PW_CHROMIUM` if Chromium is not at `/opt/pw-browsers/chromium`. The Ledger has no `package.json` (single-file, no-build rule), so Playwright must come from elsewhere.

Not covered: the page embedded in a third-party frame (AC-4.3), and a visual check of dark-theme map labels beyond token contrast (AC-5.2).
