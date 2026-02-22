# CLAUDE.md -- AI Assistant Context

## Project Overview
Personal website and blog of David Angeles-Albores, Ph.D.
Built with Jekyll and the Argon Pro theme, hosted on GitHub Pages.

## Architecture
- **Framework:** Jekyll static site generator
- **Theme:** Argon Pro by JekyllThemes.io / Creative Tim
- **Hosting:** GitHub Pages (https://dangeles.github.io)
- **Domain:** Currently using default GitHub Pages domain

## Directory Conventions
- `_pages/` -- Static pages (about, contact, projects, talks, thanks, cdecmx)
- `_posts/` -- Blog posts in `YYYY-MM-DD-PascalCaseTitle.md` format (zero-padded dates required)
- `_includes/` -- Reusable HTML partials and theme components (kebab-case naming)
- `_includes/components/` -- Modular UI components (blog/, headers/, projects/)
- `_layouts/` -- Page templates (default, page, post)
- `_data/settings.yml` -- Theme and site configuration (branding, menu, social, analytics)
- `_sass/` -- Sass stylesheet sources
- `assets/` -- Static assets (CSS, JS, fonts, images)
- `assets/img/blog/` -- Blog post images (subdirectory per post: `YYYY-MM-DD-PostTitle/`)
- `assets/img/ai_generated/` -- AI-generated images for blog/portfolio
- `images/` -- **FROZEN** legacy image directory (pre-theme-migration blog images, do NOT add new files here)
- `jupyter/` -- Rendered Jupyter notebook HTML files (linked from blog posts)
- `talks/` -- Talk PDF files
- `docs/` -- Documentation, theme license, and theme readme

## Navigation Configuration (IMPORTANT)
Navigation is defined in TWO places -- both must be updated when adding/removing pages:
1. `_config.yml` under `navigation:` -- used by some Jekyll features
2. `_data/settings.yml` under `menu_settings.menu_items:` -- used by the header template

## Image Conventions
- New blog post images go in `assets/img/blog/YYYY-MM-DD-PostTitle/`
- Site-wide images (logos, backgrounds) live in `assets/img/` subdirectories
- Legacy blog images (2015-2018) are in `images/` -- do NOT move without updating references, do NOT add new files there
- Use JPEG or WebP for photographs, PNG for graphics/diagrams, SVG for illustrations
- Never commit TIFF files or files larger than 1 MB without discussion
- **No spaces in filenames** -- use hyphens or underscores
- Use lowercase filenames and extensions

## Blog Theme Selector
The blog listing layout is controlled by `_data/settings.yml` under `blog_settings.theme`.
- `blogsHome.html` (now `blogs-home.html`) selects the layout based on this setting
- Available layouts: `grid`, `narrow`, `basic`, `basicLanding` (in `_includes/components/blog/`)

## Environment Setup (REQUIRED)

All Jekyll commands require the `pages` micromamba environment. This provides:
- Ruby 3.3.3 (at `/Users/davidangelesalbores/Y/envs/pages/`)
- Jekyll 4.3.4 (at `.../share/rubygems/bin/jekyll`)
- Bundler 2.5.21

**Activate before any build or serve command:**
```bash
micromamba activate pages       # in an interactive shell (user's normal workflow)
```

**For scripted/non-interactive use (e.g., from Claude Code Bash tool):**
```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages
```

Do NOT use the system Ruby (`/usr/bin/ruby` -- it is 2.6, too old) or attempt
`micromamba run -n pages` (gem paths are not set correctly without activation).

## Build Commands

Always run with `pages` env activated (see above):
```
bundle exec jekyll serve        # Local development server (http://localhost:4000)
bundle exec jekyll build        # Build static site to _site/
bundle install                  # Only needed after Gemfile changes
```

## Active Worktrees

This repo uses a git worktree for major refactoring work:

| Branch | Path | Purpose |
|--------|------|---------|
| `master` | `/Users/davidangelesalbores/repos/dangeles.github.io/` | Live site (GitHub Pages deploys from here) |
| `refactor/website-major` | `.worktrees/refactor/website-major/` | Major site refactor (isolated) |

The `.worktrees/` directory is gitignored. Build commands work identically in both
directories -- just activate the `pages` env and run `bundle exec jekyll serve`.

## Branch Routing Rules (READ THIS BEFORE MAKING ANY CHANGE)

**Default: if in doubt, ask before touching `master`.**

### Make changes on `master` when:
- Writing or editing a **blog post** (`_posts/`)
- Fixing a **typo or broken link** in existing content
- Adding **talk PDFs** or other static assets unrelated to the refactor
- Updating `_data/settings.yml` for **content-only** changes (e.g., social links, bio text)
- Any change that should go **live immediately** on dangeles.github.io

### Make changes on `refactor/website-major` (the worktree) when:
- Modifying **layouts** (`_layouts/`)
- Modifying **includes/components** (`_includes/`)
- Changing **Sass/CSS** (`_sass/`, `assets/css/`)
- Restructuring **navigation** or site-wide configuration (`_config.yml`, `_data/settings.yml` structure)
- Moving, renaming, or reorganizing **directories**
- Any change that would **break or visually alter** the live site during development

### Ambiguous cases -- always ask:
- Changes to `index.html` or `blog/index.html` (could be content or structural)
- New pages in `_pages/` (content, but may require nav changes that belong in refactor)
- Dependency or plugin changes (`Gemfile`)

### Merging `refactor/website-major` back to `master`:
1. Run `bundle exec jekyll build` in the worktree -- must succeed with zero errors
2. Visually verify with `bundle exec jekyll serve` (check nav, posts, images)
3. Confirm navigation consistent in both `_config.yml` and `_data/settings.yml`
4. Open a PR on GitHub for final diff review before merging
5. Use **rebase merge** (clean history) or **squash merge** (if WIP commits are messy)
6. After merge, verify GitHub Actions build succeeds before closing the PR

## Key Files
- `_config.yml` -- Jekyll configuration (collections, permalinks, plugins, navigation)
- `_data/settings.yml` -- Theme settings (branding, menu, social links, analytics)
- `index.html` -- Homepage (uses landing theme with blog listing)
- `blog/index.html` -- Blog listing page with pagination

## Content Guidelines
- Blog posts use front matter: title, date, description, author, featured_image
- Pages use front matter: title, subtitle, description, featured_image, permalink
- Use `{{ '/path/to/image' | relative_url }}` for image references in templates
- Blog posts from 2015-2018 use hardcoded absolute URLs (legacy, not ideal)

## Git Conventions
- Do not commit: `_site/`, `.jekyll-cache/`, `*.sqlite`, `*.js.map`, `.DS_Store`
- Do not commit large binary files (>1 MB) without discussion
- Post filenames must use zero-padded dates: `YYYY-MM-DD-Title.md`

## Scaling Notes
- `_posts/` supports year subdirectories (e.g., `_posts/2025/`) if the directory grows large
- For non-blog images, consider `assets/img/projects/YYYY-ProjectName/` convention
