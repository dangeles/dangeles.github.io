# Website Refactor Design
**Date:** 2026-02-28
**Branch:** refactor/website-major
**Status:** Approved — ready for implementation

---

## Goal

A simple, clean, professional personal website that makes it immediately clear who David Angeles-Albores is and what he does. The site should serve four audiences equally: academic collaborators, biotech investors, potential hires, and scientific peers.

---

## Design Approach: Option B — Michaillat structure + Genesis.bio aesthetic

The site takes Pascal Michaillat's content-first academic minimalism as a structural model and applies the visual language of genesis.bio (the company site): neutral black/white/gray palette, serif headings, generous white space, minimal navigation.

**Reference sites:**
- Structure/content: https://pascalmichaillat.org
- Visual aesthetic: https://genesis.bio

---

## Information Architecture

**Navigation (4 items):**
```
About · Research · Writing · Contact
```

| Page | URL | Content |
|------|-----|---------|
| Homepage | `/` | Dark hero + short bio + 3 recent posts + contact CTA |
| About | `/about` | Photo, full bio, credentials, expertise, personal note |
| Research | `/research` | Publications, talks, outreach (cdecmx) |
| Writing | `/writing` | Chronological post list — title, date, one-line description |
| Contact | `/contact` | Formspree form + links (LinkedIn, Scholar, Genesis) |

**Pages retired/folded:**
- `/projects` → folds into `/research`
- `/talks` → folds into `/research`
- `/cdecmx` → one paragraph in `/research` under Outreach

**URL preservation:**
- All `_posts/` URLs preserved — no redirects needed
- Blog listing moves from `/blog` to `/writing`

---

## Visual Design

### Color Palette
```
Background:    #ffffff
Text:          #1a1a1a
Subtle text:   #808285  (genesis.bio gray — dates, labels, captions)
Dividers:      #e8e8e8
Hero bg:       #0f0f0f
Hero text:     #ffffff
Links:         #1a1a1a underlined — no accent color
```

### Typography
```
Headings:   Cormorant Garamond (Google Fonts) — serif, matches genesis.bio tone
Body:       Inter (Google Fonts) — clean sans-serif
Code:       JetBrains Mono (Google Fonts)
```

### Layout Rules
- Single centered column, max-width `680px`
- Line-height `1.75`, generous paragraph spacing
- No sidebar, no card grids, no thumbnail images on listing pages
- Section dividers: single `1px` rule, nothing decorative
- Mobile-first; desktop widens margins only

### Homepage Layout
```
┌─────────────────────────────────────────┐
│  [dark bg: #0f0f0f]                     │
│  David Angeles-Albores, Ph.D.  [serif]  │
│  Executive & Founder Scientist          │
│  The Organogenesis and Tissue           │
│  Replacement Lab                        │
│                                         │
│  "I bridge computation and biology      │
│   to advance tissue replacement."       │
│                                         │
│  genesis.bio ↗   Google Scholar ↗       │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│  [white bg: #ffffff]                    │
│  Short bio (3 sentences)                │
│  Caltech · MIT · eGenesis · Altos       │
│                                         │
│  Recent writing                         │
│  ── Title ···················· Jan 2025 │
│  ── Title ···················· Oct 2024 │
│  ── Title ···················· Sep 2024 │
│  → All writing                          │
│                                         │
│  Get in touch → contact                 │
└─────────────────────────────────────────┘
```

---

## Content

### Homepage hero (approved)
- Name: David Angeles-Albores, Ph.D.
- Title: Executive & Founder Scientist
- Tagline: "I bridge computation and biology to advance tissue replacement."
- Links: genesis.bio ↗ · Google Scholar ↗

### Homepage bio (approved)
> I trained as a molecular geneticist at Caltech and MIT, then built computational biology programs at eGenesis — contributing to the first pig-to-human kidney transplant — and led AI/ML initiatives at Altos Labs. Now I serve as Executive & Founder Scientist at [Genesis](https://genesis.bio), an interdisciplinary laboratory working on the biology and computation of tissue replacement. My research spans single-cell genomics, machine learning, and the experimental frameworks that connect them.

### About page
- Keep existing content; update two things:
  1. Opening paragraph: replace "AI/ML consultant" with current role at Genesis
  2. Professional Background: add Genesis as current role above eGenesis/Altos

### Research page (new)
- Publications: clean list (title · venue · year · PDF/link)
- Talks: moved from `/talks` — restyled as list
- Outreach: one paragraph on cdecmx + link

### Writing page
- All 30+ posts preserved at existing URLs
- Listing: plain title/date list grouped by year
- No thumbnails, no featured images

### Contact page
- Keep Formspree form
- Add: LinkedIn, Google Scholar, Genesis links

---

## Technical Implementation

### Theme
Replace Argon Pro (Bootstrap-heavy) with a custom lean Jekyll layout:
- ~200 lines of CSS total
- No JavaScript except contact form
- Google Fonts only
- No unused component CSS or JS map files

### Files to rewrite
| File | Action |
|------|--------|
| `_layouts/default.html` | Rewrite — new nav, footer, no Bootstrap |
| `_layouts/page.html` | Rewrite — clean single-column |
| `_layouts/post.html` | Rewrite — readable article layout |
| `_sass/_variables.scss` | Rewrite — new palette and type scale |
| `assets/css/main.scss` | Rewrite — new styles |
| `_includes/header.html` | Rewrite — 4-item nav |
| `_includes/footer.html` | Rewrite — minimal |
| `index.html` | Rewrite — dark hero + bio + recent posts |
| `_pages/about.md` | Update content only |
| `_pages/research.md` | New page — replaces projects + talks |
| `blog/index.html` | Move to `writing/index.html`, restyled |
| `_data/settings.yml` | Simplify — remove unused theme flags |

### Files untouched
- All `_posts/` — zero changes, all URLs preserved
- `talks/` PDFs
- `assets/img/`
- `jupyter/`
- Contact form configuration (`_pages/contact.md`, Formspree)

### Branch strategy
- All work on `refactor/website-major` worktree
- Merge to `master` only after full visual review and clean build
- Merge method: rebase or squash merge
