# Soil source for the Mycelium site

The marketing site is generated from Soil with `core/ui`'s HTML forms. The
static assets (`assets/`, `robots.txt`, `sitemap.xml`) live in `public/` and are
copied or served as-is.

## Build

Provide the bootstrap compiler and build:

```sh
SOIL_LANG=/path/to/soil-lang site/build.sh
```

`site/vendor/prelude.soil` and `site/vendor/ui.soil` are pinned copies of the
core files needed by the site so this repository can build without a second
checkout. Update them deliberately when the compiler core changes.

## Layout

- `site/site.soil` — shared document shell, header, footer, and page helpers.
- `site/pages/*.soil` — one entry point per page.
- `site/build.sh` — compiles each page into `public/`.
- `public/assets/site.css` and `site.js` — the design and progressive enhancement.
