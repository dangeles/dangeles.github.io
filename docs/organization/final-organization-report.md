# Organization Report: dangeles.github.io

**Date:** 2026-02-16
**Workflow:** archive-workflow v1.0

## Summary

This report documents the comprehensive organization of the dangeles.github.io Jekyll site repository. The workflow identified and addressed significant clutter (~330 MB of reclaimable tracked files), naming convention violations, structural inconsistencies, and missing documentation.

## What Was Done

### Phase 1: Zero-Risk Cleanup (~330 MB savings)

**Gitignore fixes:**
- Fixed `__pychache__/` typo to `__pycache__/`
- Added explicit `.jekyll-cache/` pattern
- Added trailing slash to `_site/`
- Removed duplicate `data/` entry
- Added `*.sqlite`, `*.js.map`, `.claude/` patterns

**Build artifacts removed from tracking (3 files):**
- `jupyter/.pybiomart.sqlite` (5 MB pybiomart cache)
- `jupyter/cdc_state_counts.csv` (392 KB data file)
- `assets/js/argon-design-system.js.map` (source map)

**Theme demo content removed (6 files):**
- 4 unpublished example pages (`blog-grid-example.md`, `blog-list-example.md`, `blog-narrow-example.md`, `headings.md`)
- `_includes/demo-post.md`
- `_includes/disqus.html` (unused 10+ year old integration)

**Unused theme components removed (21 files):**
- `_includes/components/features/` (7 files)
- `_includes/components/pricing/` (5 files)
- `_includes/components/testimonials/` (2 files)
- `_includes/components/projects/team-carousel-3.html`, `team-carousel-4.html`, `team-carousel-5.html`
- `_includes/components/headers/header-1.html`, `header-2.html`, `header-3.html`
- `_includes/components/accordion.html`

**Unreferenced images removed (~315 MB):**
- `assets/img/presentation-page/` (72 theme demo files, ~25 MB)
- `assets/img/docs/` (2 files)
- 12 stock faces, 17 stock pages, 23 stock theme, 18 stock sections images
- 13 root-level stock images in `assets/img/`
- 1 unused brand image
- 44 unreferenced images from `images/` directory (~150 MB of camera exports)

### Phase 2: Structural Moves

**File relocations:**
- `cdecmx.md` moved to `_pages/cdecmx.md` (permalink preserved, zero URL change)
- `_LICENSE.md` moved to `docs/THEME-LICENSE.md`
- `_README.md` moved to `docs/THEME-README.md`

**Post filename normalization (7 files):**
All post filenames now use zero-padded dates per Jekyll convention:
- `2015-2-14` -> `2015-02-14`
- `2015-3-31` -> `2015-03-31`
- `2016-06-6` -> `2016-06-06`
- `2016-7-31` -> `2016-07-31`
- `2016-8-8` -> `2016-08-08`
- `2024-10-9` -> `2024-10-09`
- `2025-1-02` -> `2025-01-02`

**Include file rename:**
- `_includes/blogsHome.html` -> `_includes/blogs-home.html` (4 references updated in `index.html`)

### Phase 3: TIFF Conversion

Converted 3 referenced TIFF images to JPEG (~39 MB -> ~1 MB):
- `assets/img/faces/david.tiff` -> `david.jpeg`
- `assets/img/sections/zorro_gg.tiff` -> `zorro_gg.jpeg`
- `assets/img/pseudomonas.tiff` -> `pseudomonas.jpeg`

Updated references in:
- `_data/settings.yml`
- `_includes/blogs-home.html`
- `_includes/components/projects/team-carousel-2.html`

### Phase 4: Documentation

**New files created:**
- `CLAUDE.md` -- AI assistant context with project overview, conventions, and build commands
- `_pages/talks.md` -- Talks page linking to 5 existing talk PDFs
- `docs/organization/final-organization-report.md` -- This report
- `.archive-metadata.yaml` -- Machine-readable archival guidelines

**Configuration updates:**
- Added "Talks" to navigation in both `_config.yml` and `_data/settings.yml`

## Naming Conventions Established

| Category | Convention |
|----------|-----------|
| Blog posts | `YYYY-MM-DD-PascalCaseTitle.md` (zero-padded dates) |
| Pages | `lowercase-kebab-case.md` |
| Includes | `lowercase-kebab-case.html` |
| Layouts | `lowercase.html` |
| Sass | `_lowercase-with-hyphens.scss` |
| Blog images | `assets/img/blog/YYYY-MM-DD-PostTitle/` |
| General images | lowercase, no spaces, JPEG/PNG/WebP/SVG only |

## Items Deferred

The following improvements were identified but deferred for future work:

1. **Uppercase `.JPG` extension normalization** -- 19+ files in `images/` use `.JPG` instead of `.jpg`
2. **Camera export filename renaming** -- Referenced images still have opaque camera names (P*.JPG, IMG_*.jpg)
3. **Jupyter HTML file renaming** -- Mixed PascalCase/snake_case naming
4. **Image directory consolidation** -- `images/` (legacy) could be merged into `assets/img/blog/`
5. **Hardcoded absolute URL fixes** -- Some old posts use `https://dangeles.github.io/images/...` instead of relative URLs
6. **CodeQL workflow review** -- `.github/workflows/codeql-analysis.yml` may be unnecessary for a static site
7. **LICENSE copyright update** -- Currently credits Barry Clark (Jekyll Now author)

## Impact

- **Files removed:** ~230 files
- **Estimated space savings:** ~330 MB of tracked files
- **URL breakage:** Zero (all moves preserved permalinks)
- **New features:** Talks page with navigation
- **Documentation:** CLAUDE.md, organization report, archive metadata
