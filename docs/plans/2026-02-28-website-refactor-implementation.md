# Website Refactor Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the Argon Pro / Bootstrap site with a custom lean Jekyll layout matching the Michaillat + genesis.bio aesthetic: neutral palette, serif headings, 680px centered column, minimal JS.

**Architecture:** Custom Jekyll layouts and ~200 lines of CSS. No Bootstrap, no jQuery, no Argon Pro JS plugins. Google Fonts (Cormorant Garamond + Inter). Jekyll paginate, sitemap, and seo-tag plugins are retained. All `_posts/` URLs preserved.

**Tech Stack:** Jekyll 4.3.4, Ruby 3.3.3, Sass (SCSS), Google Fonts, Formspree, `pages` micromamba env.

**Working directory:** `.worktrees/refactor/website-major/` — all commands run from here.

**Build command:** `eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll build`

**Serve command:** `eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001`

---

## Task 1: Update _config.yml and _data/settings.yml

**Files:**
- Modify: `_config.yml`
- Modify: `_data/settings.yml`

**Step 1: Update `_config.yml`**

Replace the full file with:

```yaml
title: "David Angeles-Albores, Ph.D."
description: "Executive & Founder Scientist at The Organogenesis and Tissue Replacement Lab. Computational biologist working at the intersection of ML/AI, single-cell genomics, and tissue replacement."
url: https://dangeles.github.io
baseurl: ""
lang: en

author:
  name: "David Angeles-Albores"
  url: "https://dangeles.github.io"

social:
  links:
    - https://github.com/dangeles
    - https://www.linkedin.com/in/dangelesgenetics

collections:
  pages:
    output: true
    permalink: /:name
  posts:
    output: true
    permalink: /blog/:slug
    type: "post"

defaults:
  - scope:
      path: ""
    values:
      layout: "default"
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "default"
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"

sass:
  sass_dir: _sass
  style: compressed
  sourcemap: never

plugins:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-seo-tag

paginate: 20
paginate_path: "/writing/page:num/"

navigation:
  - text: "About"
    url: "/about"
  - text: "Research"
    url: "/research"
  - text: "Writing"
    url: "/writing"
  - text: "Contact"
    url: "/contact"
```

**Step 2: Simplify `_data/settings.yml`**

Replace the full file with:

```yaml
basic_settings:
  site_title: "David Angeles-Albores"
  favicon_image: "/assets/img/favicon.png"

contact_settings:
  form_action: "https://formspree.io/davidangelesalbores@gmail.com"
  confirmation_url: "/thanks"
  email_subject: "Contact form submission"
  send_button_text: "Send Message"

social_settings:
  github_url: "https://github.com/dangeles"
  linkedin_url: "https://www.linkedin.com/in/dangelesgenetics"
  scholar_url: "https://scholar.google.es/citations?hl=en&pli=1&user=03C2DtQAAAAJ"
  genesis_url: "https://genesis.bio"

advanced_settings:
  analytics_code: G-ESQ24FE2J1

authors:
  david:
    name: David
    picture: /assets/img/faces/david.jpeg
```

**Step 3: Verify build**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll build 2>&1 | tail -5
```

Expected: build succeeds (may have warnings about missing layouts — those will be fixed in subsequent tasks).

**Step 4: Commit**

```bash
git add _config.yml _data/settings.yml
git commit -m "refactor: update config and settings for minimal redesign"
```

---

## Task 2: CSS Foundation — Variables and Reset

**Files:**
- Modify: `_sass/_variables.scss`
- Keep: `_sass/_reset.scss` (no changes needed)
- Create: `assets/css/main.scss`

**Step 1: Rewrite `_sass/_variables.scss`**

```scss
// Typography
$font-serif: 'Cormorant Garamond', Georgia, serif;
$font-sans: 'Inter', system-ui, -apple-system, sans-serif;
$font-mono: 'JetBrains Mono', 'Courier New', monospace;

$font-size-base: 18px;
$line-height-base: 1.75;

// Colors
$color-bg: #ffffff;
$color-text: #1a1a1a;
$color-muted: #808285;
$color-divider: #e8e8e8;
$color-hero-bg: #0f0f0f;
$color-hero-text: #ffffff;
$color-link: #1a1a1a;

// Layout
$max-width: 680px;
$nav-height: 60px;

// Spacing scale
$space-xs: 0.5rem;
$space-sm: 1rem;
$space-md: 2rem;
$space-lg: 4rem;
$space-xl: 6rem;

// Breakpoints
$bp-mobile: 640px;
```

**Step 2: Create `assets/css/main.scss`**

This file must have empty front matter so Jekyll processes it:

```scss
---
---

@import "variables";
@import "reset";
@import "base";
@import "nav";
@import "hero";
@import "home";
@import "post";
@import "listing";
@import "research";
@import "contact";
@import "highlights";
```

**Step 3: Create `_sass/_base.scss`**

```scss
*, *::before, *::after {
  box-sizing: border-box;
}

html {
  font-size: $font-size-base;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: $font-sans;
  font-size: 1rem;
  line-height: $line-height-base;
  color: $color-text;
  background-color: $color-bg;
  margin: 0;
  padding: 0;
}

// Typography
h1, h2, h3, h4, h5, h6 {
  font-family: $font-serif;
  font-weight: 400;
  line-height: 1.2;
  margin-top: $space-md;
  margin-bottom: $space-sm;
  color: $color-text;
}

h1 { font-size: 2.4rem; }
h2 { font-size: 1.8rem; }
h3 { font-size: 1.4rem; }
h4 { font-size: 1.2rem; }

p {
  margin-top: 0;
  margin-bottom: $space-sm;
}

a {
  color: $color-link;
  text-decoration: underline;
  text-underline-offset: 3px;

  &:hover {
    opacity: 0.65;
  }
}

// Utility
.content-wrap {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 $space-sm;
}

hr {
  border: none;
  border-top: 1px solid $color-divider;
  margin: $space-md 0;
}

img {
  max-width: 100%;
  height: auto;
}

// Muted text
.muted {
  color: $color-muted;
  font-size: 0.875rem;
}

// Screen-reader only
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

// Google Fonts import
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Inter:wght@400;500&family=JetBrains+Mono&display=swap');
```

**Step 4: Verify `_sass/_highlights.scss` exists** — it is referenced by the import. If it does not contain valid SCSS for Jekyll's syntax highlighting, replace its contents with:

```scss
// Syntax highlighting (Monokai-inspired, minimal)
.highlight {
  background: #f8f8f8;
  border-radius: 4px;
  padding: $space-sm;
  overflow-x: auto;
  font-family: $font-mono;
  font-size: 0.85rem;
  line-height: 1.5;
  margin-bottom: $space-sm;
}

code {
  font-family: $font-mono;
  font-size: 0.875em;
  background: #f4f4f4;
  padding: 0.1em 0.3em;
  border-radius: 3px;
}

pre code {
  background: none;
  padding: 0;
}
```

**Step 5: Build check**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll build 2>&1 | grep -E "error|Error|warn" | head -20
```

Expected: zero errors (warnings about unknown tags are OK at this stage).

**Step 6: Commit**

```bash
git add _sass/_variables.scss _sass/_base.scss _sass/_highlights.scss assets/css/main.scss
git commit -m "refactor: add new CSS foundation — variables, base, font imports"
```

---

## Task 3: Navigation — Header and Footer

**Files:**
- Rewrite: `_includes/header.html`
- Rewrite: `_includes/footer.html`
- Create: `_sass/_nav.scss`

**Step 1: Rewrite `_includes/header.html`**

```html
<a href="#main" class="sr-only sr-only-focusable">Skip to main content</a>
<header class="site-header">
  <nav class="nav-inner content-wrap" aria-label="Main navigation">
    <a href="{{ '/' | relative_url }}" class="site-title">{{ site.data.settings.basic_settings.site_title }}</a>
    <button class="nav-toggle" aria-controls="nav-links" aria-expanded="false" aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-links" id="nav-links">
      {% for item in site.navigation %}
      <li>
        <a href="{{ item.url | relative_url }}"{% if page.url == item.url %} aria-current="page"{% endif %}>
          {{ item.text }}
        </a>
      </li>
      {% endfor %}
    </ul>
  </nav>
</header>
```

**Step 2: Rewrite `_includes/footer.html`**

```html
<footer class="site-footer">
  <div class="footer-inner content-wrap">
    <hr>
    <div class="footer-row">
      <span class="muted">© {{ 'now' | date: "%Y" }} David Angeles-Albores</span>
      <nav class="footer-links" aria-label="Footer navigation">
        {% if site.data.settings.social_settings.genesis_url %}
        <a href="{{ site.data.settings.social_settings.genesis_url }}" target="_blank" rel="noopener">Genesis</a>
        {% endif %}
        {% if site.data.settings.social_settings.linkedin_url %}
        <a href="{{ site.data.settings.social_settings.linkedin_url }}" target="_blank" rel="noopener">LinkedIn</a>
        {% endif %}
        {% if site.data.settings.social_settings.github_url %}
        <a href="{{ site.data.settings.social_settings.github_url }}" target="_blank" rel="noopener">GitHub</a>
        {% endif %}
        {% if site.data.settings.social_settings.scholar_url %}
        <a href="{{ site.data.settings.social_settings.scholar_url }}" target="_blank" rel="noopener">Scholar</a>
        {% endif %}
      </nav>
    </div>
  </div>
</footer>
```

**Step 3: Create `_sass/_nav.scss`**

```scss
// Site header
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: $color-bg;
  border-bottom: 1px solid $color-divider;
  height: $nav-height;
  display: flex;
  align-items: center;
}

.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.site-title {
  font-family: $font-serif;
  font-size: 1.1rem;
  font-weight: 400;
  text-decoration: none;
  color: $color-text;
  white-space: nowrap;

  &:hover {
    opacity: 0.65;
  }
}

.nav-links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: $space-md;

  li a {
    font-family: $font-sans;
    font-size: 0.875rem;
    text-decoration: none;
    color: $color-muted;
    letter-spacing: 0.03em;
    transition: color 0.15s;

    &:hover,
    &[aria-current="page"] {
      color: $color-text;
    }
  }
}

// Mobile hamburger (hidden on desktop)
.nav-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: $space-xs;

  span {
    display: block;
    width: 22px;
    height: 2px;
    background: $color-text;
  }
}

@media (max-width: $bp-mobile) {
  .nav-toggle {
    display: flex;
  }

  .nav-links {
    display: none;
    position: absolute;
    top: $nav-height;
    left: 0;
    right: 0;
    background: $color-bg;
    flex-direction: column;
    gap: 0;
    border-bottom: 1px solid $color-divider;
    padding: $space-sm 0;

    &.is-open {
      display: flex;
    }

    li a {
      display: block;
      padding: $space-xs $space-sm;
      font-size: 1rem;
    }
  }
}

// Site footer
.site-footer {
  margin-top: $space-xl;
  padding-bottom: $space-md;
}

.footer-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: $space-sm;
  padding: $space-sm 0;
}

.footer-links {
  display: flex;
  gap: $space-md;

  a {
    font-size: 0.875rem;
    color: $color-muted;
    text-decoration: none;

    &:hover {
      color: $color-text;
    }
  }
}
```

**Step 4: Add mobile nav toggle script**

This small inline script handles the hamburger toggle. It will be added to the default layout in Task 4.

**Step 5: Build check**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll build 2>&1 | tail -5
```

**Step 6: Commit**

```bash
git add _includes/header.html _includes/footer.html _sass/_nav.scss
git commit -m "refactor: new minimal header and footer — 4-item nav, no Bootstrap"
```

---

## Task 4: Default Layout

**Files:**
- Rewrite: `_layouts/default.html`

**Step 1: Rewrite `_layouts/default.html`**

```html
<!DOCTYPE html>
<html lang="{{ site.lang | default: 'en' }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% if page.url == "/" %}{{ site.title }}{% else %}{{ page.title }} — {{ site.data.settings.basic_settings.site_title }}{% endif %}</title>
  <meta name="description" content="{{ page.description | default: site.description }}">
  <link rel="shortcut icon" href="{{ site.data.settings.basic_settings.favicon_image | relative_url }}">
  <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">

  {% seo %}

  {% if site.advanced_settings.analytics_code %}
  <script async src="https://www.googletagmanager.com/gtag/js?id={{ site.data.settings.advanced_settings.analytics_code }}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', '{{ site.data.settings.advanced_settings.analytics_code }}');
  </script>
  {% endif %}
</head>

<body>
  {% include header.html %}

  <main id="main">
    {{ content }}
  </main>

  {% include footer.html %}

  <script>
    // Mobile nav toggle
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    if (toggle && links) {
      toggle.addEventListener('click', function() {
        const expanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', String(!expanded));
        links.classList.toggle('is-open');
      });
    }
  </script>
</body>
</html>
```

**Step 2: Build check**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll build 2>&1 | tail -5
```

**Step 3: Serve and visually inspect nav**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001
```

Open http://localhost:4001. Verify:
- [ ] Nav renders with 4 links (About, Research, Writing, Contact)
- [ ] Site title links to homepage
- [ ] No Bootstrap styles loading (inspect Network tab — no bootstrap.min.css)
- [ ] Footer shows Genesis, LinkedIn, GitHub, Scholar links

**Step 4: Commit**

```bash
git add _layouts/default.html
git commit -m "refactor: new default layout — no Bootstrap, minimal JS, Google Fonts"
```

---

## Task 5: Homepage

**Files:**
- Rewrite: `index.html`
- Create: `_sass/_hero.scss`
- Create: `_sass/_home.scss`

**Step 1: Rewrite `index.html`**

```html
---
title: Home
layout: default
description: "David Angeles-Albores, Ph.D. — Executive & Founder Scientist at The Organogenesis and Tissue Replacement Lab."
---

<section class="hero">
  <div class="hero-inner">
    <h1 class="hero-name">David Angeles-Albores, Ph.D.</h1>
    <p class="hero-role">Executive &amp; Founder Scientist</p>
    <p class="hero-org">The Organogenesis and Tissue Replacement Lab</p>
    <p class="hero-tagline">I bridge computation and biology to advance tissue replacement.</p>
    <div class="hero-links">
      <a href="{{ site.data.settings.social_settings.genesis_url }}" class="hero-link" target="_blank" rel="noopener">genesis.bio ↗</a>
      <a href="{{ site.data.settings.social_settings.scholar_url }}" class="hero-link" target="_blank" rel="noopener">Google Scholar ↗</a>
    </div>
  </div>
</section>

<div class="home-body content-wrap">
  <section class="home-bio">
    <p>I trained as a molecular geneticist at Caltech and MIT, then built computational biology programs at eGenesis — contributing to the first pig-to-human kidney transplant — and led AI/ML initiatives at Altos Labs. Now I serve as Executive &amp; Founder Scientist at <a href="{{ site.data.settings.social_settings.genesis_url }}" target="_blank" rel="noopener">Genesis</a>, an interdisciplinary laboratory working on the biology and computation of tissue replacement. My research spans single-cell genomics, machine learning, and the experimental frameworks that connect them.</p>
    <p class="bio-credentials muted">Ph.D. Biochemistry &amp; Molecular Biophysics, Caltech &nbsp;·&nbsp; Postdoc, MIT &nbsp;·&nbsp; eGenesis &nbsp;·&nbsp; Altos Labs</p>
  </section>

  <hr>

  <section class="home-writing">
    <h2>Recent writing</h2>
    <ul class="post-list">
      {% for post in site.posts limit:5 %}
      <li class="post-list-item">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="muted">{{ post.date | date: "%b %Y" }}</span>
      </li>
      {% endfor %}
    </ul>
    <a href="{{ '/writing' | relative_url }}" class="all-link">All writing →</a>
  </section>

  <hr>

  <section class="home-contact">
    <p>Interested in collaborating, hiring, or just getting in touch? <a href="{{ '/contact' | relative_url }}">Reach out.</a></p>
  </section>
</div>
```

**Step 2: Create `_sass/_hero.scss`**

```scss
.hero {
  background-color: $color-hero-bg;
  color: $color-hero-text;
  padding: $space-xl $space-sm;
}

.hero-inner {
  max-width: $max-width;
  margin: 0 auto;
}

.hero-name {
  font-family: $font-serif;
  font-size: 2.6rem;
  font-weight: 300;
  color: $color-hero-text;
  margin-top: 0;
  margin-bottom: $space-xs;

  @media (max-width: $bp-mobile) {
    font-size: 2rem;
  }
}

.hero-role {
  font-family: $font-sans;
  font-size: 1rem;
  color: rgba($color-hero-text, 0.7);
  margin-bottom: 0.25rem;
  letter-spacing: 0.02em;
}

.hero-org {
  font-family: $font-sans;
  font-size: 0.9rem;
  color: rgba($color-hero-text, 0.5);
  margin-bottom: $space-md;
  letter-spacing: 0.02em;
}

.hero-tagline {
  font-family: $font-serif;
  font-size: 1.4rem;
  font-style: italic;
  color: rgba($color-hero-text, 0.85);
  margin-bottom: $space-md;
  line-height: 1.4;
}

.hero-links {
  display: flex;
  gap: $space-md;
  flex-wrap: wrap;
}

.hero-link {
  font-family: $font-sans;
  font-size: 0.875rem;
  color: rgba($color-hero-text, 0.6);
  text-decoration: none;
  letter-spacing: 0.04em;
  transition: color 0.15s;

  &:hover {
    color: $color-hero-text;
    opacity: 1;
  }
}
```

**Step 3: Create `_sass/_home.scss`**

```scss
.home-body {
  padding-top: $space-lg;
  padding-bottom: $space-lg;
}

.home-bio {
  p {
    font-size: 1.05rem;
    line-height: $line-height-base;
  }
}

.bio-credentials {
  font-size: 0.85rem !important;
}

.home-writing {
  h2 {
    font-size: 1rem;
    font-family: $font-sans;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: $color-muted;
    margin-top: $space-md;
    margin-bottom: $space-sm;
  }
}

.post-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.post-list-item {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: $space-sm;
  padding: 0.5rem 0;
  border-bottom: 1px solid $color-divider;

  &:last-child {
    border-bottom: none;
  }

  a {
    text-decoration: none;
    color: $color-text;
    font-size: 0.95rem;

    &:hover {
      text-decoration: underline;
      text-underline-offset: 3px;
    }
  }

  .muted {
    white-space: nowrap;
    flex-shrink: 0;
  }
}

.all-link {
  display: inline-block;
  margin-top: $space-sm;
  font-size: 0.875rem;
  color: $color-muted;
  text-decoration: none;

  &:hover {
    color: $color-text;
  }
}

.home-contact {
  p {
    color: $color-muted;
    font-size: 0.95rem;
  }

  a {
    color: $color-text;
  }
}
```

**Step 4: Build and serve**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001
```

Open http://localhost:4001 and verify:
- [ ] Dark hero section renders with correct text hierarchy
- [ ] Bio paragraph renders below hero
- [ ] 5 most recent posts listed with dates
- [ ] "All writing →" link present
- [ ] Page is readable on mobile (resize browser)

**Step 5: Commit**

```bash
git add index.html _sass/_hero.scss _sass/_home.scss
git commit -m "feat: new homepage — dark hero, bio, recent posts"
```

---

## Task 6: Page and Post Layouts

**Files:**
- Rewrite: `_layouts/page.html`
- Rewrite: `_layouts/post.html`
- Create: `_sass/_post.scss`

**Step 1: Rewrite `_layouts/page.html`**

```html
---
layout: default
---

<div class="page-wrap content-wrap">
  {% if page.title %}
  <header class="page-header">
    <h1 class="page-title">{{ page.title }}</h1>
    {% if page.subtitle %}<p class="page-subtitle muted">{{ page.subtitle }}</p>{% endif %}
  </header>
  <hr>
  {% endif %}
  <div class="page-content">
    {{ content }}
  </div>
</div>
```

**Step 2: Rewrite `_layouts/post.html`**

```html
---
layout: default
---

<article class="post-wrap content-wrap">
  <header class="post-header">
    <h1 class="post-title">{{ page.title }}</h1>
    <p class="post-meta muted">
      {{ page.date | date: "%B %-d, %Y" }}
      {% if page.author %} · {{ page.author }}{% endif %}
    </p>
  </header>
  <hr>
  <div class="post-content">
    {{ content }}
  </div>
  <hr>
  <nav class="post-nav muted">
    {% if page.previous.url %}
    <a href="{{ page.previous.url | relative_url }}">← {{ page.previous.title }}</a>
    {% endif %}
    {% if page.next.url %}
    <a href="{{ page.next.url | relative_url }}" style="margin-left: auto">{{ page.next.title }} →</a>
    {% endif %}
  </nav>
</article>
```

**Step 3: Create `_sass/_post.scss`**

```scss
// Shared page styles
.page-wrap,
.post-wrap {
  padding-top: $space-lg;
  padding-bottom: $space-lg;
}

.page-header,
.post-header {
  margin-bottom: $space-md;
}

.page-title,
.post-title {
  font-size: 2rem;
  margin-top: 0;
  margin-bottom: $space-xs;

  @media (max-width: $bp-mobile) {
    font-size: 1.6rem;
  }
}

.page-subtitle {
  font-size: 1rem;
  margin-top: 0;
}

.post-meta {
  font-size: 0.875rem;
  margin: 0;
}

// Post body content
.post-content,
.page-content {
  h2 { font-size: 1.5rem; margin-top: $space-lg; }
  h3 { font-size: 1.2rem; margin-top: $space-md; }

  blockquote {
    border-left: 3px solid $color-divider;
    margin: $space-md 0;
    padding: $space-xs $space-sm;
    color: $color-muted;
    font-style: italic;

    p { margin-bottom: 0; }
  }

  ul, ol {
    padding-left: $space-md;
    margin-bottom: $space-sm;
  }

  li {
    margin-bottom: 0.25rem;
  }

  img {
    display: block;
    margin: $space-md auto;
    border-radius: 3px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: $space-sm;
    font-size: 0.9rem;

    th, td {
      padding: 0.5rem $space-xs;
      border-bottom: 1px solid $color-divider;
      text-align: left;
    }

    th {
      font-weight: 500;
      color: $color-muted;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
  }
}

// Post nav
.post-nav {
  display: flex;
  justify-content: space-between;
  font-size: 0.875rem;
  padding-top: $space-sm;

  a {
    text-decoration: none;
    color: $color-muted;

    &:hover { color: $color-text; }
  }
}
```

**Step 4: Build and verify posts render**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001
```

Open any blog post, e.g., http://localhost:4001/blog/2025-01-02-NoncanonicalFolateSignaling and verify:
- [ ] Post title renders in serif
- [ ] Date shows below title
- [ ] Body content readable with correct line height
- [ ] Previous/next navigation at bottom

**Step 5: Commit**

```bash
git add _layouts/page.html _layouts/post.html _sass/_post.scss
git commit -m "refactor: new page and post layouts — clean single-column"
```

---

## Task 7: About Page

**Files:**
- Modify: `_pages/about.md`

**Step 1: Update front matter and opening of `_pages/about.md`**

Update only these two things — leave everything else verbatim:

1. Replace the subtitle line:
   - Old: `subtitle: A computational biologist musing about genetics and evolution using AI`
   - New: `subtitle: Executive & Founder Scientist · The Organogenesis and Tissue Replacement Lab`

2. Replace the opening two paragraphs (lines 12–18) with:

```markdown
Hi! I'm David Angeles-Albores — Executive & Founder Scientist at [Genesis](https://genesis.bio), an interdisciplinary laboratory working on the biology and computation of tissue replacement. I am a computational biologist with expertise in ML/AI and single-cell genomics, with a unique background that spans wet-lab molecular genetics and quantitative computational analysis.

My goal as a scientist and leader is to bridge computation and biology: to translate complex biological data into actionable insights, and to build experimental frameworks capable of generating the training data that powers the next generation of AI/ML models in biomedicine.
```

3. In the **Professional Background** section, add Genesis as the first bullet before eGenesis:

```markdown
- **Genesis (The Organogenesis and Tissue Replacement Lab)**: Founder and Executive & Founder Scientist. Building the computational and biological foundations of organ and tissue replacement.
```

**Step 2: Build and verify**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001
```

Open http://localhost:4001/about and verify:
- [ ] Subtitle shows new role
- [ ] Opening paragraph mentions Genesis
- [ ] Genesis listed first in Professional Background

**Step 3: Commit**

```bash
git add _pages/about.md
git commit -m "content: update about page — current role at Genesis, updated intro"
```

---

## Task 8: Research Page

**Files:**
- Create: `_pages/research.md`
- Create: `_sass/_research.scss`

**Step 1: Create `_pages/research.md`**

Content sourced from `_includes/components/projects/team-carousel-1.html`, `team-carousel-2.html`, and `_pages/talks.md`:

```markdown
---
layout: default
title: Research
subtitle: Selected projects, publications, and talks
permalink: /research/
---

<div class="research-wrap content-wrap">

## Industry Projects

<div class="research-list">

### Computationally designed promoters for pig humanization
*eGenesis*

I computationally designed promoters to drive pig pan-tissue transgene expression by identifying pan-expressed genes, generating synthetic promoters, and testing their activity. I demonstrated through experimental and computational analyses that our promoters were tissue-specific — a key finding that reframed the silencing hypothesis and contributed to the first compassionate use pig-to-human kidney transplant.

**Methods:** RNA-seq · ATAC-seq · PHASTcons

<a href="https://www.nature.com/articles/s41586-023-06594-4" target="_blank" rel="noopener">Read the paper ↗</a>

---

### Analyses of cellular programming in aging
*Altos Labs*

As Sr. Computational Scientist, I led a matrixed team of four wet-lab scientists to perform translational studies of cellular programming. I developed computational pipelines to study the mechanism of action of our molecule of interest, designed experiments to test our hypotheses, and oversaw their execution.

**Methods:** Single-cell RNA-seq · Tool development · Cross-functional leadership

---

### Multimodal AI initiatives
*Altos Labs*

I conceptualized and led the formation of a cross-functional team to develop multimodal machine learning models. I led the team to develop ML models, collect training data, and develop experimental methods for data collection.

**Methods:** AI/ML development · Cross-functional leadership

</div>

---

## Talks

<div class="talks-list">

- **Worm Meeting 2021** — [View PDF]({{ '/talks/WormMeeting2021.pdf' | relative_url }})
- **Transcriptomes as Phenotypes** — ASBMB, May 2019 — [View PDF]({{ '/talks/20190509.ASBMB.TranscriptomesAsPhenotypes.pdf' | relative_url }})
- **Transcriptomes as Phenotypes** — ASBMB, May 2018 — [View PDF]({{ '/talks/20180509.ASBMB.TranscriptomesAsPhenotypes.pdf' | relative_url }})
- **Hanna H. Gray Fellowship** — HHMI — [Talk PDF]({{ '/talks/HannaHGrayTalk.pdf' | relative_url }}) · [Script PDF]({{ '/talks/HannaHGrayScript.pdf' | relative_url }})

</div>

---

## Outreach

### Clubes de Ciencia México

I have been an active participant, contributor, and instructor with [*Clubes de Ciencia*](https://www.clubesdeciencia.mx/), a graduate-student-led initiative that brings intensive science workshops to students across Mexico. My workshops have covered genetics, molecular biology, and evolutionary biology. I co-discovered a new planarian species — *Dugesia guanajuatensis* — with students during a 2016 workshop in Guanajuato. [Full story →]({{ '/cdc.html' | relative_url }})

</div>
```

**Step 2: Create `_sass/_research.scss`**

```scss
.research-wrap {
  padding-top: $space-lg;
  padding-bottom: $space-lg;

  h2 {
    font-size: 1rem;
    font-family: $font-sans;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: $color-muted;
    margin-top: $space-lg;
    margin-bottom: $space-sm;
  }

  h3 {
    font-size: 1.2rem;
    margin-top: $space-md;
    margin-bottom: $space-xs;
  }
}

.research-list,
.talks-list {
  p {
    font-size: 0.95rem;
    color: $color-text;
    margin-bottom: $space-xs;
  }

  em {
    color: $color-muted;
    font-style: normal;
    font-size: 0.875rem;
  }

  strong {
    font-size: 0.8rem;
    color: $color-muted;
    font-weight: 400;
    font-family: $font-sans;
    letter-spacing: 0.03em;
    text-transform: uppercase;
  }

  a {
    font-size: 0.875rem;
    color: $color-muted;

    &:hover { color: $color-text; }
  }
}

.talks-list {
  list-style: none;
  padding: 0;

  li {
    padding: 0.5rem 0;
    border-bottom: 1px solid $color-divider;
    font-size: 0.95rem;

    &:last-child { border-bottom: none; }
  }
}
```

**Step 3: Build and verify**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001
```

Open http://localhost:4001/research and verify:
- [ ] Three industry projects render correctly
- [ ] Talks list with PDF links
- [ ] Outreach section at bottom

**Step 4: Commit**

```bash
git add _pages/research.md _sass/_research.scss
git commit -m "feat: new research page — projects, talks, outreach in single clean page"
```

---

## Task 9: Writing Listing Page

**Files:**
- Create: `writing/index.html`
- Create: `_sass/_listing.scss`

**Step 1: Create `writing/index.html`**

```html
---
layout: default
title: Writing
description: "Essays and notes by David Angeles-Albores on computational biology, machine learning, and science."
paginate: 20
---

<div class="listing-wrap content-wrap">
  <header class="page-header">
    <h1 class="page-title">Writing</h1>
    <p class="page-subtitle muted">Essays and notes on computation, biology, and science.</p>
  </header>
  <hr>

  {% assign posts_by_year = paginator.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
  {% for year_group in posts_by_year %}
  <section class="year-group">
    <h2 class="year-label">{{ year_group.name }}</h2>
    <ul class="post-list">
      {% for post in year_group.items %}
      <li class="post-list-item">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="muted">{{ post.date | date: "%b %-d" }}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endfor %}

  {% if paginator.total_pages > 1 %}
  <nav class="pagination muted" aria-label="Pagination">
    {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | relative_url }}">← Newer</a>
    {% endif %}
    <span>Page {{ paginator.page }} of {{ paginator.total_pages }}</span>
    {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | relative_url }}">Older →</a>
    {% endif %}
  </nav>
  {% endif %}
</div>
```

**Step 2: Create `_sass/_listing.scss`**

```scss
.listing-wrap {
  padding-top: $space-lg;
  padding-bottom: $space-lg;
}

.year-group {
  margin-bottom: $space-md;
}

.year-label {
  font-family: $font-sans;
  font-size: 0.8rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: $color-muted;
  margin-top: $space-md;
  margin-bottom: $space-xs;
}

.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.875rem;
  padding-top: $space-md;
  border-top: 1px solid $color-divider;

  a {
    text-decoration: none;
    color: $color-muted;

    &:hover { color: $color-text; }
  }
}
```

**Step 3: Build and verify**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001
```

Open http://localhost:4001/writing and verify:
- [ ] Posts listed grouped by year
- [ ] Each entry: title (linked) + date
- [ ] All 30+ posts visible

Also verify a post URL is still correct: http://localhost:4001/blog/2025-01-02-NoncanonicalFolateSignaling — should load fine.

**Step 4: Commit**

```bash
git add writing/index.html _sass/_listing.scss
git commit -m "feat: new /writing listing page — chronological by year, no thumbnails"
```

---

## Task 10: Contact Page

**Files:**
- Modify: `_pages/contact.md`

**Step 1: Update `_pages/contact.md`**

Replace the front matter and add links section. Keep the existing Formspree form HTML. The updated file should be:

```markdown
---
layout: default
title: Contact
description: "Get in touch with David Angeles-Albores."
permalink: /contact/
---

<div class="content-wrap" style="padding-top: 3rem; padding-bottom: 3rem;">

<p>I'm always happy to hear from researchers, collaborators, founders, and students. Fill in the form below or find me through the links at the bottom of this page.</p>

{% include contact-form.html %}

<hr>

<p class="muted" style="font-size: 0.875rem;">
  <a href="{{ site.data.settings.social_settings.linkedin_url }}" target="_blank" rel="noopener">LinkedIn</a> &nbsp;·&nbsp;
  <a href="{{ site.data.settings.social_settings.scholar_url }}" target="_blank" rel="noopener">Google Scholar</a> &nbsp;·&nbsp;
  <a href="{{ site.data.settings.social_settings.genesis_url }}" target="_blank" rel="noopener">Genesis</a> &nbsp;·&nbsp;
  <a href="{{ site.data.settings.social_settings.github_url }}" target="_blank" rel="noopener">GitHub</a>
</p>

</div>
```

**Step 2: Verify `_includes/contact-form.html` still works**

The existing contact form include uses Formspree — it should work without changes. Build and open http://localhost:4001/contact to confirm the form renders.

**Step 3: Commit**

```bash
git add _pages/contact.md
git commit -m "content: update contact page — add social links, clean intro"
```

---

## Task 11: Final Cleanup and Build Verification

**Files:**
- Modify: `_config.yml` (if paginate_path needs adjustment)
- Remove: unused includes

**Step 1: Full build with zero-error check**

```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll build 2>&1
```

Expected: `done in X seconds` with no `ERROR` lines. Warnings about liquid are acceptable.

**Step 2: Verify all critical URLs**

Start the server and check each:
```bash
eval "$(micromamba shell hook --shell=zsh)" && micromamba activate pages && bundle exec jekyll serve --port 4001
```

- [ ] http://localhost:4001/ — homepage with dark hero
- [ ] http://localhost:4001/about — about page
- [ ] http://localhost:4001/research — research page
- [ ] http://localhost:4001/writing — writing listing
- [ ] http://localhost:4001/contact — contact page with form
- [ ] http://localhost:4001/blog/2025-01-02-NoncanonicalFolateSignaling — post URL preserved
- [ ] http://localhost:4001/blog/2024-10-28-GeneralizationIsHard — another post URL preserved
- [ ] http://localhost:4001/cdc.html — cdecmx page still accessible

**Step 3: Mobile check**

In browser DevTools, toggle device toolbar (iPhone SE size). Verify:
- [ ] Nav collapses to hamburger on mobile
- [ ] Hero text readable at small sizes
- [ ] Post list items don't overflow
- [ ] No horizontal scroll

**Step 4: Remove now-unused Argon Pro includes**

These files are no longer referenced by any layout or page:
```bash
git rm _includes/blogs-home.html
git rm _includes/blogs.html
git rm _includes/home-sample.html
git rm _includes/socials.html
git rm _includes/svg-icons.html
git rm _includes/meta.html
git rm -r _includes/components/
```

Note: do NOT remove `_includes/contact-form.html` — it is used by the contact page.
Note: do NOT remove `_includes/head.html` if it exists and is referenced — check first with `grep -r "include head.html" _layouts/`.

**Step 5: Final commit**

```bash
git add -A
git commit -m "refactor: remove unused Argon Pro includes and components"
```

**Step 6: Push refactor branch**

```bash
git push -u origin refactor/website-major
```

---

## Definition of Done

- [ ] `bundle exec jekyll build` exits with zero errors
- [ ] All 5 pages render correctly in browser
- [ ] All existing `/blog/:slug` post URLs load correctly
- [ ] Nav works on desktop and mobile
- [ ] No Bootstrap CSS or JS loading
- [ ] Footer shows Genesis, LinkedIn, GitHub, Scholar
- [ ] Homepage bio matches approved text exactly
- [ ] Branch pushed to origin; PR opened for final review before merge to master
