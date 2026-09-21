# Asterline Labs website

Public portfolio, beta landing pages, support material, and product-specific privacy policies for Asterline Labs.

## Live site

After GitHub Pages deployment:

- Home: `https://brandonewade-debug.github.io/asterline-labs/`
- Support: `https://brandonewade-debug.github.io/asterline-labs/support/`
- Privacy center: `https://brandonewade-debug.github.io/asterline-labs/privacy/`
- Terms: `https://brandonewade-debug.github.io/asterline-labs/terms/`

## Products shown

- Orbit — external TestFlight beta
- Nova Stream — external TestFlight beta
- Console Bridge — private beta
- CueForge — development prototype
- DockerOS — in development

The public TestFlight links are stored only in `content.py`. Console Bridge intentionally has no public TestFlight link because App Store Connect does not currently expose one.

## Build

The site uses the Python standard library and static HTML, CSS, JavaScript, SVG, and PNG assets. No package manager, web framework, analytics SDK, cookie banner, or external font is required.

```bash
python3 build.py
```

Generated output is written to `docs/`, which is the GitHub Pages publishing directory.

Approved Orbit, Nova Stream, and Console Bridge icon exports are stored under `static/apps/`, so the website repository builds without access to the private application repositories. Replace those exports only with approved artwork.

## Preview

Because the production site is a GitHub project page, links use the `/asterline-labs/` base path. One local preview method is:

```bash
mkdir -p /tmp/asterline-preview
ln -s "$PWD/docs" /tmp/asterline-preview/asterline-labs
python3 -m http.server 8765 --directory /tmp/asterline-preview
```

Then open `http://127.0.0.1:8765/asterline-labs/`.

## Brand files

Approved files are in `docs/assets/brand/`:

- `asterline-mark.svg` — primary transparent vector mark
- `asterline-mark-1024.png` — transparent raster mark
- `asterline-lockup.svg` — horizontal mark and wordmark
- `asterline-lockup.png` — transparent horizontal raster lockup

See `BRAND.md` for color and usage guidance.

## Privacy and legal maintenance

The site has one website policy and a separate privacy policy for each product. Policies are generated from `content.py`. Update the effective date whenever the substance changes.

The policies describe the repositories as inspected on September 21, 2026. They must be reviewed again whenever a product adds a developer-operated backend, analytics, advertising, account creation, a new third-party SDK, a new OAuth scope, external AI processing, or materially different storage or deletion behavior.

`APPLE-COMPLIANCE-CHECKLIST.md` records the current App Store and TestFlight preflight items. It is a practical engineering checklist, not a substitute for current Apple policy review or legal advice.

## Ownership

Copyright © 2026 Asterline Labs / Brandon Wade. All rights reserved. No open-source license is granted by this repository unless a file explicitly says otherwise.
