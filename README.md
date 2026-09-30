# Vanessa Interiors — Website

Static multipage website (HTML / CSS / JavaScript). No build step or server code is needed — upload the whole folder to any web host.

## Structure

```
index.html  about.html  services.html  portfolio.html  gallery.html  blog.html
contact.html  faqs.html  testimonials.html  privacy-policy.html  terms.html
cost-estimator.html  404.html
services/   11 service subpages (home-interiors.html … turnkey-interiors.html)
portfolio/  residential.html  commercial.html  villas.html  apartments.html
css/        style.css (base, header, footer) · components.css · responsive.css
js/         config.js · main.js · calculator.js · popup.js · whatsapp.js · forms.js · gallery.js · portfolio.js
images/     logo/ · services/ (illustrations) · hero/ · portfolio/ · gallery/
assets/     company profile / catalogue PDFs (to be added)
```

## Everyday changes — all in `js/config.js`

| What | Where |
| --- | --- |
| WhatsApp number, phone, email, address | `SITE_CONFIG` |
| Base estimator rate (₹1,600/sq.ft.) | `COST_PER_SQFT` |
| A different rate for one category | `INTERIOR_PRICES`, e.g. `kitchen: 1800,` |
| Receive form enquiries by email/server | `SITE_CONFIG.formEndpoint` (see below) |

The rate is shown on the estimator cards automatically — nothing else to edit.

## How the lead system works

- **Any button** with `data-lead="Service Name"` opens the compact enquiry popup with that service pre-selected (`openLeadPopup("Modular Kitchen")`). Add `data-lead-title="Book Site Visit"` to change the popup heading.
- **Any button** with `data-whatsapp="Service Name"` opens WhatsApp with the service-specific message (`openWhatsApp("Modular Kitchen")`). Leave the value empty for a general message.
- **Estimator** → *Discuss This Estimate on WhatsApp* sends type, area, property, style, timeline and estimated cost (`openEstimateWhatsApp()`).
- **Form submissions** (popup + contact page): if `formEndpoint` is empty, WhatsApp opens with all the enquiry details filled in. To also receive enquiries by email, create a free form endpoint (e.g. Formspree or a Google Apps Script web app) and paste its URL into `formEndpoint` — enquiries are then POSTed as JSON.

## Before going live — please complete

1. **Project photographs** — add genuine photos to `images/gallery/` and `images/portfolio/`, then list them in `js/gallery.js` (`GALLERY_ITEMS`) and `js/portfolio.js` (`PORTFOLIO_PROJECTS`). Remove the placeholder illustration entries from the gallery once real photos are in.
2. **Testimonials** — `testimonials.html` has a commented template. Publish only verified reviews with client permission.
3. **Privacy Policy & Terms** — replace `[Insert Date]` with the effective date and have both reviewed for your actual practices.
4. **Warranty** — the site says warranty/support is "according to the applicable project terms". Add specific durations only once confirmed.
5. **Social links** — only Instagram (@vanessainteriorsindia) is linked. Add Facebook / YouTube / LinkedIn to the footer when the pages are live.
6. **Company profile / catalogue PDFs** — add to `assets/` and link them.
7. **Blog** — the 20 topics are listed as "coming soon". Publish each as a full article and link it from `blog.html`.
8. Set the web server to use `404.html` as the not-found page.

## Animations

All motion lives in two files — `css/animations.css` and `js/animations.js` — loaded on every page. Nothing else depends on them: delete the two `<link>`/`<script>` lines and the site works exactly as before, just static.

- **Scroll reveals** use IntersectionObserver and the reusable classes `.reveal`, `.reveal-left`, `.reveal-right`, `.reveal-scale`, `.reveal-fade`, `.stagger-item`, `.img-reveal`. The script applies them automatically to the site's existing sections, cards and grids; you can also add a class to any new element by hand.
- **Tuning:** distance, duration and stagger are CSS variables at the top of `animations.css` (`--reveal-distance`, `--reveal-duration`, `--stagger-step`). Mobile uses shorter values automatically.
- **Reduced motion:** visitors who ask their device for reduced motion get the fully static site.

## `_build-tools/` (optional, not needed for hosting)

The pages were generated from `content.py` (all page text) with `build.py`, so the header, footer and menus stay identical everywhere. To change menu items or page text across the site, edit `content.py` / `build.py` and run `python3 build.py ..` from inside `_build-tools/`. You can also simply edit the HTML files directly.
