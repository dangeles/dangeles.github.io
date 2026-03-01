# The Axonometric — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement the "Axonometric" aesthetic redesign — asymmetric left-shifted column, biological accent color on links, and lighter hero name weight.

**Architecture:** Four surgical SCSS edits across three files. No layout restructuring, no HTML changes, no JS changes. The asymmetry is achieved entirely with CSS `clamp()` and a `min-width: 1000px` media query. Below 1000px the layout stays centered; above 1000px the column shifts left, leaving an architectural void on the right.

**Tech Stack:** Jekyll 4.3.4, SCSS (compiled by jekyll-sass-converter), Google Fonts (Spectral + Inter + JetBrains Mono), micromamba `pages` environment (Ruby 3.3.3).

---

## Context: How this codebase works

- SCSS files live in `_sass/`. The entry point is `assets/css/main.scss` (imports all partials).
- Variables are in `_sass/_variables.scss` — imported first by all other partials.
- `.content-wrap` is the layout container used sitewide AND by the nav (`<nav class="nav-inner content-wrap">` in `_includes/header.html`). Updating `.content-wrap` automatically aligns the nav with the content column.
- `.hero-inner` in `_sass/_hero.scss` is the width-constrained inner container of the full-bleed dark hero section. It needs its own asymmetric margin because it is not a `.content-wrap`.
- Google Fonts are imported via `@import url(...)` in `_sass/_base.scss` line 99. Font weights must be listed in the URL or they won't load.
- Build command (non-interactive shell): `export PATH="/Users/davidangelesalbores/Y/envs/pages/bin:$PATH" && bundle exec jekyll build`
- Working directory for all commands: `/Users/davidangelesalbores/repos/dangeles.github.io/`
- Branch: `master` (CSS changes go here per branch routing rules — refactor worktree is behind).

---

## Task 1: Add accent color variable and update max-width

**Files:**
- Modify: `_sass/_variables.scss`

### Step 1: Edit `_sass/_variables.scss`

Make two changes:

**Change A** — reduce `$max-width`:
```scss
// BEFORE (line 19):
$max-width: 680px;

// AFTER:
$max-width: 600px;
```

**Change B** — add `$color-accent` before `$color-link` and update `$color-link` to reference it:
```scss
// BEFORE (lines 16-16):
$color-link: #1a1a1a;

// AFTER — insert $color-accent above, update $color-link:
$color-accent: hsl(160, 22%, 37%);  // biological trace — aged copper-green
$color-link: $color-accent;
```

The final Colors block should look like this:
```scss
// Colors
$color-bg: #ffffff;
$color-text: #1a1a1a;
$color-muted: #6b6b6b;
$color-divider: #e8e8e8;
$color-hero-bg: #0f0f0f;
$color-hero-text: #ffffff;
$color-accent: hsl(160, 22%, 37%);  // biological trace — aged copper-green
$color-link: $color-accent;
```

### Step 2: Build to verify no errors

```bash
cd /Users/davidangelesalbores/repos/dangeles.github.io
export PATH="/Users/davidangelesalbores/Y/envs/pages/bin:$PATH" && bundle exec jekyll build
```

Expected: `done in X.XXX seconds.` with no errors or warnings about undefined variables.

### Step 3: Commit

```bash
git add _sass/_variables.scss
git commit -m "feat(design): add biological accent color, narrow column to 600px

Introduces $color-accent hsl(160,22%,37%) — aged copper-green used for links.
Updates $color-link to reference accent. Narrows $max-width 680px → 600px.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 2: Update link styles and asymmetric column in `_base.scss`

**Files:**
- Modify: `_sass/_base.scss`

### Step 1: Update the `a` (link) styles

**BEFORE** (lines 44–52):
```scss
a {
  color: $color-link;
  text-decoration: underline;
  text-underline-offset: 3px;

  &:hover {
    opacity: 0.65;
  }
}
```

**AFTER:**
```scss
a {
  color: $color-link;
  text-decoration: none;

  &:hover {
    text-decoration: underline;
    text-underline-offset: 3px;
  }
}
```

Rationale: Links are now the biological accent color ($color-link = $color-accent). The underline appears on hover only — the color itself doesn't change. This matches the design decision: "the page doesn't announce it; you find it." The `opacity: 0.65` hover is removed because it looked faded on a green color.

### Step 2: Update `.content-wrap` with asymmetric margin

**BEFORE** (lines 62–66):
```scss
.content-wrap {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 $space-sm;
}
```

**AFTER:**
```scss
.content-wrap {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 $space-sm;

  @media (min-width: 1000px) {
    margin-left: clamp(2rem, 18vw, 200px);
    margin-right: auto;
  }
}
```

How this works:
- Below 1000px: `margin: 0 auto` centers the column (default, safe).
- Above 1000px: `margin-left` overrides to `clamp(2rem, 18vw, 200px)`. At 1000px this is 180px; at 1111px it hits the 200px cap; above 1111px the right void grows as viewport widens.
- `margin-right: auto` absorbs the remaining space on the right (the architectural void).
- Because the nav uses `<nav class="nav-inner content-wrap">`, it automatically aligns to the same axis — no separate nav changes needed.

### Step 3: Add Spectral weight 200 to Google Fonts URL

**BEFORE** (line 99):
```scss
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;0,500;1,400&family=Inter:ital,wght@0,400;0,500;1,400;1,500&family=JetBrains+Mono&display=swap');
```

**AFTER** — add `0,200;` to the Spectral weight list:
```scss
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,200;0,300;0,400;0,500;1,400&family=Inter:ital,wght@0,400;0,500;1,400;1,500&family=JetBrains+Mono&display=swap');
```

This is required: without requesting weight 200, browsers substitute the nearest available weight (300) and the hero name visually stays the same.

### Step 4: Build to verify no errors

```bash
export PATH="/Users/davidangelesalbores/Y/envs/pages/bin:$PATH" && bundle exec jekyll build
```

Expected: clean build with no SCSS compilation errors.

### Step 5: Commit

```bash
git add _sass/_base.scss
git commit -m "feat(design): asymmetric column layout and accent link color

.content-wrap shifts left of center above 1000px viewport using
clamp(2rem, 18vw, 200px) left margin — architectural void on the right.
Links use biological accent color with hover-only underline.
Spectral weight 200 added to Google Fonts request.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Task 3: Update hero — align to column axis and lighten name weight

**Files:**
- Modify: `_sass/_hero.scss`

### Step 1: Update `.hero-inner` with matching asymmetric margin

**BEFORE** (lines 7–10):
```scss
.hero-inner {
  max-width: $max-width;
  margin: 0 auto;
}
```

**AFTER:**
```scss
.hero-inner {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 $space-sm;

  @media (min-width: 1000px) {
    margin-left: clamp(2rem, 18vw, 200px);
    margin-right: auto;
  }
}
```

Note: Adding `padding: 0 $space-sm` here to match `.content-wrap` — without it, the hero text sits flush against the viewport edge on small screens (no horizontal breathing room). The media query must match the breakpoint in Task 2 exactly (`1000px`).

### Step 2: Update `.hero-name` to weight 200

**BEFORE** (line 15):
```scss
font-weight: 300;
```

**AFTER:**
```scss
font-weight: 200;
```

Full `.hero-name` block context for reference:
```scss
.hero-name {
  font-family: $font-serif;
  font-size: 2.6rem;
  font-weight: 200;       // was 300
  color: $color-hero-text;
  margin-top: 0;
  margin-bottom: $space-xs;

  @media (max-width: $bp-mobile) {
    font-size: 2rem;
  }
}
```

### Step 3: Build to verify no errors

```bash
export PATH="/Users/davidangelesalbores/Y/envs/pages/bin:$PATH" && bundle exec jekyll build
```

Expected: clean build, no errors.

### Step 4: Visual check (manual)

Start a local server and open in browser:

```bash
export PATH="/Users/davidangelesalbores/Y/envs/pages/bin:$PATH" && bundle exec jekyll serve
```

Open `http://localhost:4000` and verify:
- [ ] On a wide browser window (≥1000px): content column is visibly left of center with empty right space
- [ ] Hero name appears lighter/thinner than before
- [ ] Links in the bio paragraph (e.g., "The Organogenesis and Tissue Replacement Lab") are green, no underline
- [ ] Hovering a body link shows underline (accent color stays the same on hover)
- [ ] Hero links ("genesis.bio ↗", "Google Scholar ↗") remain white/grey — not green
- [ ] Nav links remain grey — not green
- [ ] Footer links remain grey — not green
- [ ] Narrowing browser below 1000px: column re-centers cleanly
- [ ] Narrowing below 640px: mobile layout is clean

### Step 5: Commit

```bash
git add _sass/_hero.scss
git commit -m "feat(design): align hero to column axis, hero name weight 200

.hero-inner uses same asymmetric clamp margin as .content-wrap above
1000px — hero text and body content share one vertical spine.
.hero-name font-weight 300 → 200 for architectural incision effect.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Verification Checklist

After all three tasks are committed:

- [ ] `bundle exec jekyll build` passes with zero errors
- [ ] Column is visibly left-shifted on ≥1000px screens (right margin is clearly larger than left margin)
- [ ] Column re-centers on <1000px screens
- [ ] Biological accent color appears on in-content links only
- [ ] Nav links, hero links, footer links retain their original colors (no accent bleed)
- [ ] Hero name is lighter (weight 200 vs previous 300)
- [ ] No regressions on post pages, writing listing, about, contact, talks pages
- [ ] Mobile layout (≤640px) is clean

---

## Rollback

If anything goes wrong:

```bash
git log --oneline -5   # find the commit SHA before Task 1
git reset --hard <SHA-before-task-1>
```

All changes are in `_sass/` only — no content, no HTML, no config. Safe to revert.
