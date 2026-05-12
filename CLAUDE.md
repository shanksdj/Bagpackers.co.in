# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Static HTML website for **Goa Trip Packages** (`goatrippackages.in`) — a Goa-based travel/tour operator. Deployed on Vercel. No build framework; pages are plain HTML files served directly.

## Asset minification

The only dev tooling is CSS/JS minification:

```bash
# Minify a CSS file
npx cleancss -o css/site.bundle.min.css css/site.bundle.css

# Minify a JS file
npx uglifyjs js/custom-script.js -o js/site.bundle.min.js
```

`css/site.bundle.min.css` and `js/site.bundle.min.js` are hand-maintained vendor bundles. Edit their source counterparts, then re-minify.

## Architecture

### Page structure
Each HTML page is self-contained. All pages share a common `<head>` pattern:
1. GTM + Facebook Pixel scripts (deferred pixel load via scroll/pointer events)
2. Critical CSS loaded synchronously (`bootstrap.css`)
3. Non-critical CSS loaded asynchronously via `media="print" onload="this.media='all'"`
4. SEO block (`<!-- SEO & Performance: generated block -->`) containing `<title>`, meta tags, canonical, OG/Twitter tags, and JSON-LD schema
5. `css/site-optimizations.css` loaded async last

### CSS layers
| File | Purpose |
|------|---------|
| `css/bootstrap.css` | Bootstrap 4 grid/components |
| `css/style.css` | Primary theme styles |
| `css/responsive.css` | Breakpoint overrides |
| `css/site-optimizations.css` | Overrides for sticky CTA buttons, disables legacy float button, suppresses WOW animations until JS marks them allowed |
| `css/site.bundle.min.css` | Minified vendor bundle (OWL Carousel, FancyBox, jQuery UI, icon fonts, etc.) |

### JS layers
| File | Purpose |
|------|---------|
| `js/custom-script.js` | All jQuery-based UI: sticky header, mobile nav, carousels (OWL), tabs, accordion, lightbox, form validation, WOW animations |
| `js/site-optimizations.js` | Lazy-loads `data-bg` background images via IntersectionObserver; adds `noopener noreferrer` to `_blank` links |
| `js/site.bundle.min.js` | Minified vendor bundle (jQuery, Bootstrap, OWL, Isotope, FancyBox, WOW, etc.) |
| `js/map-script.js` | Google Maps embed helpers |

### Contact form
`sendemail.php` and `sendmail2.php` handle POST submissions from contact forms and redirect back to `contact.html?message=Successfull` or `?message=Failed`. These require a PHP-capable host (the Vercel deployment only serves static assets — PHP must run on a separate server or serverless function).

### SEO injection tooling
`GOATRIP/python-seo-inject.py` and `GOATRIP/seo-inject.sh` are batch scripts that insert per-page meta tags, JSON-LD schema (WebSite, WebPage, BreadcrumbList, TouristTrip), and hidden SEO copy into every HTML file. They look for the `<!-- /SEO & Performance: generated block -->` comment as the injection anchor. Run from the root directory where the HTML files live.

`fix_logos.py` performs regex replacement of logo `<img>` src attributes across all HTML files.

### Deployment
`vercel.json` sets aggressive cache headers:
- JS/CSS/fonts/images: `max-age=31536000, immutable`
- HTML/XML/TXT: `max-age=300, stale-while-revalidate=86400`

No build step — Vercel serves the repo root as a static site.

## Key page inventory

| File | Content |
|------|---------|
| `index.html` | Homepage with package listings |
| `goa-tour-package-5D-4N.html` | 5-day 4-night package |
| `goa-tour-package-4D-3N.html` | 4-day 3-night package |
| `goa-weekend-trip.html` | 3-day 2-night weekend package |
| `Goa-things-to-do.html` | Activity listings hub |
| `Scuba-Adventure.html` | Scuba diving page |
| `Water-Sports.html` | Water sports page |
| `Party-Cruise.html` | Dinner cruise page |
| `Hot-Air-Balloon-Goa.html` | Hot air balloon page |
| `sitemap.xml` | Machine-readable sitemap |
| `ror.xml` | Review-oriented Rich Snippets feed |

## Tracking IDs

- Google Tag Manager: `GTM-KZBW2ZCW`
- Facebook Pixel: `1408142280396407`
- Business phone/WhatsApp: `+918882305614`
- Contact email: `info@goatrippackages.in`
