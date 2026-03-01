# Design: "The Axonometric" — Aesthetic Redesign

**Date:** 2026-03-01
**Author:** David Angeles-Albores
**Status:** Approved

---

## Brief

Evolve the site from "competent academic minimal" toward a design that is minimalist, elegant, timeless, and signals disciplinary crossover — biology, computation, and engineering coexisting on the same canvas. Reference aesthetic: architecture office (Zaha Hadid, BIG, Herzog & de Meuron). No animation. One biological accent color.

---

## Design Decisions

### What "boundaries crossed" means visually
**Disciplinary crossover** — the design itself signals that the author operates across fields that don't normally talk to each other. Not literal boundary-breaking in layout, but the composition communicates it: architectural spatial discipline (asymmetric column, generous void) meets a single living-color trace (the biological accent).

### Reference aesthetic
Architecture office — extreme whitespace, axonometric use of negative space, high typographic contrast, near-zero color, precision over warmth.

### Color
One biological accent: `hsl(160, 22%, 37%)` ≈ `#406b5f`. Aged copper-green — the color of a petri dish held to the light, or structural patina. WCAG AA contrast ~5.1:1 on white. Used only on links in the main content area. Hero links remain white.

### Motion
None. Absolute stillness. Architecture offices rarely animate anything.

---

## Layout

**Column width:** 600px (from 680px)

**Asymmetric offset:** `clamp(2rem, 18vw, 200px)` left margin, `auto` right margin. On a 1200px viewport, the column starts at 200px from the left edge and ends at 800px — leaving 400px of architectural void on the right. On 1400px the right margin grows to 600px.

**Vertical spine:** The header nav inner container, `.hero-inner`, `.content-wrap`, and all page content share the same left offset. One invisible vertical axis runs the entire height of the page.

**Mobile collapse:** Below 640px, `margin-left: auto` re-centers the column. The asymmetry collapses cleanly; no visitor on a small screen sees anything break.

**Dark hero:** The hero's full-width `#0f0f0f` background remains unchanged. The text inside it aligns to the same 200px offset, so the name sits at the same x-position as all body content below it.

---

## Typography

**One change only:** Hero name `font-weight: 300` → `font-weight: 200`. Ultra-light type at 2.6rem reads as architectural incision. Everything else is unchanged: Spectral for headings (weight 400), Inter for body (18px/1.75), JetBrains Mono for code.

---

## Color

**New variable:** `$color-accent: hsl(160, 22%, 37%)` in `_variables.scss`.

**Applied to:** Link color only — `a { color: $color-accent }` in `_base.scss`, with hover underline.

**Not applied to:** Borders, backgrounds, decorative elements, muted text, footer, hero links (hero links override to white).

---

## Files Changed

| File | Change |
|---|---|
| `_sass/_variables.scss` | `$content-width: 600px`; add `$color-accent` |
| `_sass/_base.scss` | `.content-wrap` asymmetric margin; link color |
| `_sass/_hero.scss` | `.hero-inner` same offset; `.hero-name` weight 200; hero link color override |
| `_sass/_layout.scss` or `_sass/_header.scss` | Header nav aligns to column axis |

---

## What Doesn't Change

Body font, body size, heading weights, spacing scale, page structure and content, mobile behavior, dark hero background, footer, post layouts, contact form, JavaScript (none added).

---

## Success Criteria

- Column is visibly left-shifted on screens ≥ 900px
- Right margin reads as intentional architectural void, not a layout bug
- Accent color appears on links and only links; no other color on the page
- Hero name reads lighter and more incised at weight 200
- Mobile renders cleanly (column re-centers below 640px)
- Jekyll build passes with zero errors
- WCAG AA contrast maintained (accent color ~5.1:1 on white)
