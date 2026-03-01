# Font Design — dangeles.github.io
*Date: 2026-03-01*

## Decision

Replace **Cormorant Garamond** with **Spectral** as the heading/display serif.
Keep **Inter** for body and UI text. Keep **JetBrains Mono** for code.

## Rationale

### Why Spectral replaces Cormorant Garamond
Cormorant Garamond was inherited from the previous theme and felt borrowed rather
than personal. Spectral carries the same light, elegant, old-world character but
was designed specifically for digital reading — it renders crisper at all screen
sizes. The light weight (300) conveys the same sophistication without Cormorant's
occasional preciousness at large display sizes.

### Why Inter stays for body
The site is likely transitioning toward a portfolio format, with long-form essays
moving to Substack. Inter is optimal for short portfolio text (bio, project
descriptions, credential lists). If long-form writing remains on the site, Inter
is still readable for posts up to ~1,000 words. The swap to a warm serif body
(e.g. Lora) can be revisited if the site stays writing-focused.

### Design intent
The heading/body pairing (serif display + clean sans body) signals a multidimensional
person: the serif brings scholarly, literary weight; the sans keeps it accessible
and forward-looking. Spectral's specific character — light, precise, timeless —
suits someone who is simultaneously a rigorous scientist, an entrepreneur, and a
writer.

## Font Specification

| Role | Family | Weights loaded |
|------|--------|----------------|
| Headings, display, nav logo | Spectral | 300, 400, 500, italic 400 |
| Body, UI, meta | Inter | 400, 500, italic 400, italic 500 |
| Code | JetBrains Mono | 400 |

## Implementation

**Two file edits:**

1. `_sass/_variables.scss` line 2:
   - Before: `$font-serif: 'Cormorant Garamond', Georgia, serif;`
   - After:  `$font-serif: 'Spectral', Georgia, serif;`

2. `_sass/_base.scss` line 99 (Google Fonts import):
   - Replace `Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400` with
     `Spectral:ital,wght@0,300;0,400;0,500;1,400`

All other usage already flows through the `$font-serif` Sass variable — no other
files need changes.

## Visual verification checklist
- [ ] Hero name (Spectral 300, 2.6rem) — should feel light and refined
- [ ] Hero tagline (Spectral italic, 1.4rem) — Spectral italics are excellent
- [ ] H1 post titles (Spectral 400, 2rem)
- [ ] H2 section headings in posts (Spectral 400, 1.5rem)
- [ ] Nav site name (Spectral serif, used in nav logo)
- [ ] Blockquotes (Spectral italic via body font-style rule)
