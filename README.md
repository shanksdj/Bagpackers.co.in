# Bagpackers.co.in

**India's multi-destination travel website** — handcrafted tour packages for Goa, Manali, Shimla, Kerala and Rajasthan.

## Overview

- **Brand:** Bagpackers
- **Domain:** bagpackers.co.in
- **WhatsApp:** +91-9810467420
- **Email:** info@bagpackers.co.in
- **Tech stack:** Static HTML/CSS/JavaScript — no framework, no build step
- **Deployment:** Vercel (static hosting, see `vercel.json` for cache headers)

---

## Destinations & Packages (26 pages)

### Goa (5 pages)
| File | Package | Duration | Price |
|------|---------|----------|-------|
| `goa-packages.html` | Goa — All Packages | — | — |
| `goa-beach-holiday-package.html` | Goa Beach Holiday | 3N/4D | ₹7,999 |
| `goa-south-goa-serenity-package.html` | South Goa Serenity | 3N/4D | ₹8,499 |
| `goa-honeymoon-package.html` | Goa Honeymoon Special | 4N/5D | ₹14,999 |
| `goa-adventure-party-package.html` | Goa Adventure & Party | 3N/4D | ₹9,499 |

### Manali (5 pages)
| File | Package | Duration | Price |
|------|---------|----------|-------|
| `manali-packages.html` | Manali — All Packages | — | — |
| `manali-volvo-holiday-package.html` | Manali Volvo Holiday | 3N/4D | ₹8,499 |
| `manali-sissu-atal-tunnel-package.html` | Manali Sissu & Atal Tunnel | 4N/5D | ₹11,499 |
| `manali-honeymoon-package.html` | Manali Honeymoon | 4N/5D | ₹14,999 |
| `manali-adventure-package.html` | Manali Adventure | 3N/4D | ₹9,999 |

### Shimla (5 pages)
| File | Package | Duration | Price |
|------|---------|----------|-------|
| `shimla-packages.html` | Shimla — All Packages | — | — |
| `shimla-mall-road-holiday-package.html` | Shimla Mall Road Holiday | 3N/4D | ₹7,499 |
| `shimla-kufri-chail-package.html` | Shimla–Kufri–Chail | 4N/5D | ₹9,999 |
| `shimla-manali-combo-package.html` | Shimla–Manali Combo | 5N/6D | ₹13,999 |
| `shimla-honeymoon-package.html` | Shimla Honeymoon | 3N/4D | ₹12,999 |

### Kerala (5 pages)
| File | Package | Duration | Price |
|------|---------|----------|-------|
| `kerala-packages.html` | Kerala — All Packages | — | — |
| `kerala-backwater-houseboat-package.html` | Kerala Backwater Houseboat | 4N/5D | ₹12,999 |
| `kerala-complete-tour-package.html` | Kerala Complete Tour | 6N/7D | ₹18,999 |
| `kerala-honeymoon-package.html` | Kerala Honeymoon | 5N/6D | ₹19,999 |
| `kerala-wildlife-nature-package.html` | Kerala Wildlife & Nature | 4N/5D | ₹13,499 |

### Rajasthan (5 pages)
| File | Package | Duration | Price |
|------|---------|----------|-------|
| `rajasthan-packages.html` | Rajasthan — All Packages | — | — |
| `rajasthan-royal-heritage-package.html` | Rajasthan Royal Heritage | 5N/6D | ₹14,999 |
| `rajasthan-jaisalmer-desert-safari-package.html` | Jaipur–Jaisalmer Desert Safari | 5N/6D | ₹13,499 |
| `rajasthan-honeymoon-package.html` | Rajasthan Honeymoon | 5N/6D | ₹17,999 |
| `rajasthan-golden-triangle-package.html` | Golden Triangle + Rajasthan | 6N/7D | ₹16,999 |

### Support Pages (6 pages)
`index.html` · `about.html` · `contact.html` · `FAQ.html` · `privacy-policy.html` · `terms-and-condition.html` · `sitemap.html`

---

## Tech Stack

- **HTML5** — Plain static HTML, no templating engine
- **CSS3** — Bootstrap 4, custom `style.css`, responsive breakpoints, `site-optimizations.css`
- **JavaScript** — jQuery, OWL Carousel, FancyBox, WOW animations, custom-script.js
- **Fonts** — Google Fonts (Poppins, Playfair Display)
- **Icons** — Font Awesome, Flaticon icon fonts
- **Deployment** — Vercel (static)
- **Minification** — `cleancss` + `uglify-js` (npm devDependencies)

## CSS Layer Order
1. `css/bootstrap.css` — grid & components
2. `css/style.css` — primary theme
3. `css/responsive.css` — breakpoints
4. `css/fontawesome-all.css` — icons
5. `css/site.bundle.min.css` — vendor bundle (OWL, FancyBox, etc.)
6. `css/site-optimizations.css` — overrides, floating WhatsApp button, sticky CTAs

## Minification Commands
```bash
# CSS
npx cleancss -o css/site.bundle.min.css css/site.bundle.css

# JS
npx uglifyjs js/custom-script.js -o js/site.bundle.min.js
```

## Key Features
- Zero tracking codes (no GTM, no Facebook Pixel, no GA)
- Floating WhatsApp button on every page (number: 919810467420)
- Package-specific WhatsApp pre-filled messages
- Fully interlinked: destination pages → package pages → related packages
- Breadcrumb navigation on all pages
- Consistent header/footer/nav across all 26 pages
- Responsive (mobile-first)

---

© 2026 Bagpackers.co.in — All Rights Reserved
