"""Static site generator for the Vanessa Interiors website.
Run:  python3 build.py <output_dir>
Header, footer, popup triggers and estimator markup are defined once here and
baked into every page, so each HTML file is complete and SEO-readable."""
import json
import os
import sys
from html import escape

from content import *  # noqa: F401,F403
from icons import icon, sprite

OUT = sys.argv[1] if len(sys.argv) > 1 else ".."
PAGES = {}


def e(t):
    return escape(t, quote=True)


# ====================================================================== SHELL
def head(p, path, title, desc):
    canonical = SITE_URL + "/" + ("" if path == "index.html" else path)
    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vanessa Interiors">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/images/logo/vanessa-interiors-logo.png">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" href="{p}images/logo/favicon.png">
<link rel="apple-touch-icon" href="{p}images/logo/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&amp;family=Outfit:wght@300;400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="{p}css/style.css">
<link rel="stylesheet" href="{p}css/components.css">
<link rel="stylesheet" href="{p}css/responsive.css">
<link rel="stylesheet" href="{p}css/animations.css">
<script src="{p}js/animations.js"></script>'''


def header(p, active, service_slug=None):
    def nav_link(key, href, label):
        cur = ' aria-current="page"' if active == key else ""
        return f'<li><a class="nav-link" href="{p}{href}"{cur}>{label}</a></li>'

    cur_attr = ' aria-current="page"'
    mega_items = "".join(
        f'<li><a href="{p}services/{s["slug"]}.html"{cur_attr if s["slug"] == service_slug else ""}>'
        f'<span class="icon-tile">{icon(s["icon"])}</span><span><strong>{s["name"]}</strong><small>{e(s["short"])}</small></span></a></li>'
        for s in SERVICES)
    svc_cur = " is-current" if active == "services" else ""
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{p}index.html" aria-label="Vanessa Interiors — home">
      <img src="{p}images/logo/vanessa-interiors-logo.png" alt="Vanessa Interiors" width="911" height="370">
    </a>
    <nav class="site-nav" id="siteNav" aria-label="Main">
      <ul class="nav-list">
        {nav_link("home", "index.html", "Home")}
        {nav_link("about", "about.html", "About")}
        <li class="has-dropdown{svc_cur}">
          <button type="button" class="dropdown-toggle" aria-expanded="false" aria-controls="megaServices">Services {icon("chevron", "")}</button>
          <div class="mega" id="megaServices">
            <ul class="mega__links">{mega_items}</ul>
            <div class="mega__promo">
              <span class="eyebrow eyebrow--light">Plan your budget</span>
              <h3>Interior Cost Estimator</h3>
              <p>Enter your area and get an instant planning estimate.</p>
              <a class="btn btn--primary btn--sm" href="{p}cost-estimator.html">{icon("calc")} Estimate Cost</a>
              <a class="mega__all" href="{p}services.html">View all services →</a>
            </div>
          </div>
        </li>
        {nav_link("portfolio", "portfolio.html", "Portfolio")}
        {nav_link("gallery", "gallery.html", "Gallery")}
        {nav_link("blog", "blog.html", "Blog")}
        {nav_link("contact", "contact.html", "Contact")}
      </ul>
      <div class="nav-mobile-extra">
        <a class="btn btn--primary" href="{p}cost-estimator.html">{icon("calc")} Interior Cost Estimator</a>
        <a class="btn btn--whatsapp" href="{WA_URL}" data-whatsapp="">{icon("whatsapp")} WhatsApp Us</a>
        <a class="btn btn--ghost" href="tel:{PHONE_LINK}" data-phone-link>{icon("phone")} {PHONE}</a>
      </div>
    </nav>
    <div class="header-actions">
      <a class="header-call" href="tel:{PHONE_LINK}" data-phone-link aria-label="Call {PHONE}">{icon("phone")}<span data-phone-text>{PHONE}</span></a>
      <a class="btn btn--primary btn--sm" href="{p}cost-estimator.html">Free Estimate</a>
      <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="siteNav" aria-label="Menu"><span></span></button>
    </div>
  </div>
</header>'''


def footer(p, lead_service="General Enquiry"):
    svc = "".join(f'<li><a href="{p}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="logo-chip" href="{p}index.html"><img src="{p}images/logo/vanessa-interiors-logo.png" alt="Vanessa Interiors" width="911" height="370" loading="lazy"></a>
        <p>Vanessa Interiors is a luxury and customized interior design company in Visakhapatnam, offering residential and commercial interior solutions.</p>
        <p>From home interiors and modular kitchens to villa interiors, office design, renovation, and turnkey projects, we help clients explore personalized spaces designed around their requirements.</p>
        <div class="footer-social">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram @vanessainteriorsindia">{icon("instagram")}</a>
          <a href="{WA_URL}" data-whatsapp="" aria-label="WhatsApp">{icon("whatsapp")}</a>
        </div>
      </div>
      <div>
        <h3>Quick Links</h3>
        <ul class="footer-links">
          <li><a href="{p}index.html">Home</a></li>
          <li><a href="{p}about.html">About Us</a></li>
          <li><a href="{p}services.html">Services</a></li>
          <li><a href="{p}portfolio.html">Portfolio</a></li>
          <li><a href="{p}gallery.html">Gallery</a></li>
          <li><a href="{p}blog.html">Blog</a></li>
          <li><a href="{p}contact.html">Contact Us</a></li>
          <li><a href="{p}cost-estimator.html">Cost Estimator</a></li>
        </ul>
      </div>
      <div>
        <h3>Services</h3>
        <ul class="footer-links">{svc}</ul>
      </div>
      <div>
        <h3>Contact Information</h3>
        <ul class="footer-contact">
          <li>{icon("pin")}<span>{ADDRESS}</span></li>
          <li>{icon("phone")}<a href="tel:{PHONE_LINK}" data-phone-link>{PHONE}</a></li>
          <li>{icon("mail")}<a href="mailto:{EMAIL}" data-email-link>{EMAIL}</a></li>
          <li>{icon("globe")}<a href="{SITE_URL}">www.vanessainteriors.in</a></li>
          <li>{icon("instagram")}<a href="{INSTAGRAM}" target="_blank" rel="noopener">@vanessainteriorsindia</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© <span data-year>2026</span> Vanessa Interiors. All Rights Reserved.</p>
      <ul>
        <li><a href="{p}faqs.html">FAQs</a></li>
        <li><a href="{p}testimonials.html">Testimonials</a></li>
        <li><a href="{p}privacy-policy.html">Privacy Policy</a></li>
        <li><a href="{p}terms.html">Terms &amp; Conditions</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-rule"></div>
</footer>
<a class="float-wa" href="{WA_URL}" data-whatsapp="{e("" if lead_service == "General Enquiry" else lead_service)}" aria-label="Chat with Vanessa Interiors on WhatsApp">{icon("whatsapp")}</a>
<div class="mobile-bar" aria-label="Quick actions">
  <a class="mobile-bar__call" href="tel:{PHONE_LINK}" data-phone-link>{icon("phone")} Call</a>
  <a class="mobile-bar__wa" href="{WA_URL}" data-whatsapp="{e("" if lead_service == "General Enquiry" else lead_service)}">{icon("whatsapp")} WhatsApp</a>
  <button type="button" class="mobile-bar__quote" data-lead="{e(lead_service)}">Get Quote</button>
</div>'''


def page(path, title, desc, main, active=None, service_slug=None, scripts=(), schema=None, lead_service="General Enquiry", root=None):
    depth = path.count("/")
    p = root if root is not None else "../" * depth
    main = main.replace("{P}", p)
    js = ["config", "whatsapp", "forms", "popup", "main"] + list(scripts)
    script_tags = "\n".join(f'<script src="{p}js/{n}.js"></script>' for n in js)
    ld = ""
    if schema:
        for s in (schema if isinstance(schema, list) else [schema]):
            ld += f'\n<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
    PAGES[path] = f'''{head(p, path, title, desc)}{ld}
</head>
<body data-root="{p}">
{sprite()}
{header(p, active, service_slug)}
<main id="main">
{main}
</main>
{footer(p, lead_service)}
{script_tags}
</body>
</html>
'''


def business_schema():
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness",
        "name": "Vanessa Interiors", "url": SITE_URL, "telephone": PHONE_LINK, "email": EMAIL,
        "image": SITE_URL + "/images/logo/vanessa-interiors-logo.png", "foundingDate": "2012",
        "description": "Luxury and customized interior design company in Visakhapatnam offering residential and commercial interiors.",
        "address": {"@type": "PostalAddress", "streetAddress": "Aruna Inn, 49-24-16, Sankara Matam Road, Madhuranagar, Akkayyapalem",
                    "addressLocality": "Visakhapatnam", "addressRegion": "Andhra Pradesh", "postalCode": "530016", "addressCountry": "IN"},
        "areaServed": "Visakhapatnam", "sameAs": [INSTAGRAM],
    }


def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + "/" + h}
                                for i, (n, h) in enumerate(items)]}


# ====================================================================== PARTIALS
def crumbs(items):
    """items: [(label, href or None)] — href relative to root, with {P}."""
    lis = []
    for label, href in items:
        if href:
            lis.append(f'<li><a href="{{P}}{href}">{e(label)}</a></li>')
        else:
            lis.append(f'<li><span aria-current="page">{e(label)}</span></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'


def page_hero(crumb_items, eyebrow, h1, lead="", extra="", art=None, art_alt="", wide=False):
    art_html = ""
    if art:
        art_html = f'''<div class="page-hero__art reveal"><figure class="art-frame">
  <img src="{{P}}images/services/{art}.svg" alt="{e(art_alt)}" width="800" height="600">
  <img class="art-frame__mark" src="{{P}}images/logo/butterfly-mark.png" alt="" width="180" height="180">
</figure></div>'''
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    inner = f'''<div>
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  {lead_html}
  {extra}
</div>'''
    body = f'<div class="page-hero__grid">{inner}{art_html}</div>' if art else inner
    return f'''<section class="page-hero{" page-hero--wide" if wide else ""}">
<div class="container">
{crumbs(crumb_items)}
{body}
</div>
</section>'''


def cta_band(title, text, service="General Enquiry", primary="Get a Free Consultation", title_attr=""):
    wa_attr = "" if service == "General Enquiry" else service
    lt = f' data-lead-title="{e(title_attr)}"' if title_attr else ""
    return f'''<section class="section section--tight">
<div class="container">
<div class="cta-band reveal">
  <div>
    <h2>{title}</h2>
    <p>{text}</p>
    <a class="cta-band__phone" href="tel:{PHONE_LINK}" data-phone-link>{icon("phone")} Call Us: {PHONE}</a>
  </div>
  <div class="btn-row">
    <button type="button" class="btn btn--primary" data-lead="{e(service)}"{lt}>{primary}</button>
    <a class="btn btn--whatsapp" href="{WA_URL}" data-whatsapp="{e(wa_attr)}">{icon("whatsapp")} WhatsApp Us</a>
  </div>
</div>
</div>
</section>'''


def faq_list(pairs):
    return '<div class="faq">' + "".join(
        f'<details><summary>{e(q)}</summary><div class="faq__answer"><p>{e(a)}</p></div></details>' for q, a in pairs) + "</div>"


def service_card(s, i=None):
    num = f'<span class="service-card__num">{i:02d}</span>' if i else ""
    return f'''<a class="card card--hover service-card reveal" href="{{P}}services/{s["slug"]}.html">
  <div class="service-card__media">{num}<img src="{{P}}images/services/{s["img"]}.svg" alt="{e(s["name"])} illustration" loading="lazy" width="800" height="600"></div>
  <div class="service-card__body">
    <h3>{s["name"]}</h3>
    <p>{e(s["short"])}</p>
    <span class="link-arrow">Explore service {icon("arrow")}</span>
  </div>
</a>'''


def estimator_promo():
    return f'''<div class="card promo-card reveal">
  <span class="icon-tile">{icon("calc")}</span>
  <h3>Interior Cost Estimator</h3>
  <p>Enter your area in sq.ft. and get an instant planning estimate for your home, kitchen, wardrobes, bedroom or living area.</p>
  <a class="btn btn--primary" href="{{P}}cost-estimator.html">Estimate My Cost</a>
</div>'''


def service_mini(s):
    return f'''<a class="card card--hover service-mini" href="{{P}}services/{s["slug"]}.html">
  <span class="icon-tile">{icon(s["icon"])}</span>
  <span><h3>{s["name"]}</h3><p>{e(s["short"])}</p></span>
</a>'''


# ====================================================================== ESTIMATOR
EST_TYPES = [("completeHome", "Complete Home Interior", "home"), ("kitchen", "Kitchen", "kitchen"),
             ("wardrobes", "Wardrobes", "wardrobe"), ("bedroom", "Bedroom", "bed"), ("livingArea", "Living Area", "sofa")]
EST_PROPERTY = ["Apartment", "Villa", "Independent House"]
EST_STYLE = ["Modern", "Contemporary", "Minimalist", "Luxury", "Traditional", "Scandinavian", "Industrial"]
EST_TIMELINE = ["Immediately", "Within 1 Month", "Within 3 Months", "Within 6 Months", "Planning Stage"]
DISCLAIMER = ("Estimated cost is for initial planning purposes only. Final project pricing may vary depending on design "
              "requirements, materials, specifications, site conditions and project scope.")


def opt_group(name, options, prefix):
    return '<div class="opt-row">' + "".join(
        f'<div class="opt"><input type="radio" id="{prefix}-{i}" name="{name}" value="{e(o)}"><label for="{prefix}-{i}">{e(o)}</label></div>'
        for i, o in enumerate(options)) + "</div>"


def estimator(h="h2"):
    types = "".join(
        f'''<div class="type-card"><input type="radio" id="est-type-{k}" name="interiorType" value="{k}">
<label for="est-type-{k}"><span class="icon-tile">{icon(ic)}</span><strong>{label}</strong><small data-rate-for="{k}"></small></label></div>'''
        for k, label, ic in EST_TYPES)
    return f'''<div class="estimator-wrap">
<form class="estimator" id="estimatorForm" novalidate aria-label="Interior cost estimator">
  <fieldset class="est-step" data-est-group="interiorType">
    <legend><span class="est-step__num">1</span> What would you like to estimate?</legend>
    <div class="type-cards">{types}</div>
    <p class="est-error" data-est-error="interiorType" role="alert"></p>
  </fieldset>
  <fieldset class="est-step" data-est-group="area">
    <legend><span class="est-step__num">2</span> Enter your area <span class="est-step__hint">(sq.ft.)</span></legend>
    <div class="area-field">
      <label class="sr-only" for="estArea">Area in square feet</label>
      <input id="estArea" name="area" type="text" inputmode="decimal" autocomplete="off" placeholder="Enter area in sq.ft." aria-describedby="estAreaErr">
      <span class="area-field__unit" aria-hidden="true">sq.ft.</span>
    </div>
    <p class="est-error" id="estAreaErr" data-est-error="area" role="alert"></p>
  </fieldset>
  <fieldset class="est-step" data-est-group="propertyType">
    <legend><span class="est-step__num">3</span> Property type</legend>
    {opt_group("propertyType", EST_PROPERTY, "est-prop")}
    <p class="est-error" data-est-error="propertyType" role="alert"></p>
  </fieldset>
  <fieldset class="est-step" data-est-group="style">
    <legend><span class="est-step__num">4</span> Preferred style</legend>
    {opt_group("style", EST_STYLE, "est-style")}
    <p class="est-error" data-est-error="style" role="alert"></p>
  </fieldset>
  <fieldset class="est-step" data-est-group="timeline">
    <legend><span class="est-step__num">5</span> Project timeline</legend>
    {opt_group("timeline", EST_TIMELINE, "est-time")}
    <p class="est-error" data-est-error="timeline" role="alert"></p>
  </fieldset>
  <div class="est-submit">
    <button type="submit" class="btn btn--primary">{icon("calc")} Calculate Estimate</button>
    <p class="disclaimer">{icon("info")}<span>{DISCLAIMER}</span></p>
  </div>
</form>
<aside class="est-aside">
  <div class="estimate-result" id="estimateResult" hidden aria-live="polite">
    <p class="estimate-result__label">Your Estimated Interior Cost</p>
    <p class="estimate-result__total" data-slot="total"></p>
    <p class="estimate-result__calc">Calculation: <span data-slot="calc"></span></p>
    <dl>
      <div><dt>Interior Type</dt><dd data-slot="type"></dd></div>
      <div><dt>Area</dt><dd data-slot="area"></dd></div>
      <div><dt>Property</dt><dd data-slot="property"></dd></div>
      <div><dt>Preferred Style</dt><dd data-slot="style"></dd></div>
      <div><dt>Timeline</dt><dd data-slot="timeline"></dd></div>
    </dl>
    <button type="button" class="btn btn--whatsapp" data-whatsapp-estimate>{icon("whatsapp")} Discuss This Estimate on WhatsApp</button>
    <button type="button" class="btn btn--light" data-lead="Complete Home Interior" data-lead-title="Get Detailed Estimate" data-estimate-lead>Get Detailed Estimate</button>
    <p class="disclaimer">{icon("info")}<span>{DISCLAIMER}</span></p>
  </div>
  <div class="est-placeholder">
    <span class="icon-tile icon-tile--blue">{icon("calc")}</span>
    <{h} class="h3-display">Your estimate appears here</{h}>
    <p>Choose what you'd like to estimate, enter your area in sq.ft. and complete the steps. Your result updates instantly — no page reload.</p>
  </div>
</aside>
</div>'''


# ====================================================================== HOME
def build_home():
    services = "".join(service_card(s, i + 1) for i, s in enumerate(SERVICES)) + estimator_promo()
    why = "".join(
        f'<div class="why-card reveal{" why-card--accent" if i == 0 else ""}"><span class="icon-tile{" icon-tile--green" if i % 3 == 1 else (" icon-tile--blue" if i % 3 == 2 else "")}">{icon(ic)}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, (ic, t, d) in enumerate(WHY))
    process = "".join(f'<li class="reveal"><span class="process__step">Step {i + 1}</span><h3>{t}</h3><p>{d}</p></li>'
                      for i, (t, d) in enumerate(PROCESS))
    port = "".join(f'''<a class="cat-card card--hover reveal" href="{{P}}portfolio/{c["slug"]}.html">
<img src="{{P}}images/services/{c["img"]}.svg" alt="{c["name"]} interiors illustration" loading="lazy" width="800" height="600">
<div class="cat-card__body"><h3>{c["name"]} Interiors</h3><p>{c["card"]}</p><span class="link-arrow">View projects {icon("arrow")}</span></div></a>'''
                   for c in PORTFOLIO)
    main = f'''
<section class="hero">
<div class="container hero__grid">
  <div>
    <p class="eyebrow">Transform Your Space with Vanessa Interiors</p>
    <h1>Luxury Interiors, <em>Customized</em> for Your Lifestyle</h1>
    <p class="lead">From elegant homes to sophisticated commercial spaces, Vanessa Interiors brings together luxury design, thoughtful planning, and complete interior execution.</p>
    <p>With 14 years of experience and 100+ completed projects, we create customized interiors designed around your vision, lifestyle, and requirements.</p>
    <p class="hero__loc">{icon("pin")} Visakhapatnam | Residential &amp; Commercial Interiors</p>
    <div class="btn-row">
      <button type="button" class="btn btn--primary" data-lead="General Enquiry" data-lead-title="Get a Free Consultation">Get a Free Consultation</button>
      <a class="btn btn--outline" href="{{P}}portfolio.html">Explore Our Projects</a>
    </div>
    <div class="stats">
      <div class="stat"><strong>14</strong><span>Years of experience</span></div>
      <div class="stat"><strong>100+</strong><span>Completed projects</span></div>
      <div class="stat"><strong>50+</strong><span>Team members</span></div>
      <div class="stat"><strong>₹5L</strong><span>Projects start from</span></div>
    </div>
  </div>
  <div class="hero__art reveal">
    <figure class="art-frame">
      <img src="{{P}}images/services/living-room.svg" alt="Illustration of a luxury living room interior" width="800" height="600">
      <img class="art-frame__mark" src="{{P}}images/logo/butterfly-mark.png" alt="" width="180" height="180">
    </figure>
  </div>
</div>
</section>

<section class="section section--white">
<div class="container split">
  <div class="reveal">
    <p class="eyebrow">About Vanessa Interiors</p>
    <h2>Creating Spaces That Reflect Your Personality</h2>
    <div class="divider-rule"></div>
    <p class="lead">Your interior should be more than visually appealing. It should feel personal, functional, and designed around the way you live or work.</p>
  </div>
  <div class="reveal">
    <p>Vanessa Interiors is a luxury and customized interior design company in Visakhapatnam, offering interior design and execution services for homes, apartments, villas, offices, and commercial spaces.</p>
    <p>With 14 years of experience and a team of 50+ members, we work to deliver design solutions that balance aesthetics, functionality, and project requirements.</p>
    <p>Whether you are planning a new home interior or transforming an existing commercial space, we help bring your ideas into a structured design and execution process.</p>
    <a class="link-arrow" href="{{P}}about.html">Know More About Us {icon("arrow")}</a>
  </div>
</div>
</section>

<section class="section">
<div class="container">
  <div class="section-head section-head--split">
    <div>
      <p class="eyebrow">Our Services</p>
      <h2>Complete Interior Design Solutions for Every Space</h2>
      <p>At Vanessa Interiors, we offer customized interior design solutions for residential and commercial properties in Visakhapatnam. Our services cover individual rooms, complete homes, villas, offices, and commercial interiors.</p>
    </div>
    <a class="btn btn--outline" href="{{P}}services.html">Explore All Services</a>
  </div>
  <div class="grid grid--3">{services}</div>
</div>
</section>

<section class="section section--tint" id="estimator">
<div class="container">
  <div class="section-head section-head--center">
    <p class="eyebrow">Interior Cost Estimator</p>
    <h2>Estimate Your Interior Budget in Seconds</h2>
    <p>Select what you'd like to estimate, enter your area, and get an instant planning estimate you can discuss with our team on WhatsApp.</p>
  </div>
  {estimator("h3")}
</div>
</section>

<section class="section section--white">
<div class="container">
  <div class="section-head">
    <p class="eyebrow">Why Choose Vanessa Interiors?</p>
    <h2>Experience, Customization &amp; Attention to Detail</h2>
    <p>Choosing an interior designer is an important decision. At Vanessa Interiors, our approach focuses on understanding your requirements and delivering interior solutions suited to your project.</p>
  </div>
  <div class="why-grid">{why}
    <div class="why-card why-card--cta reveal">
      <h3>Ready to plan your space?</h3>
      <button type="button" class="btn btn--primary" data-lead="General Enquiry" data-lead-title="Book Site Visit">Book Site Visit</button>
    </div>
  </div>
</div>
</section>

<section class="section section--dark">
<div class="container">
  <div class="section-head">
    <p class="eyebrow eyebrow--light">Our Interior Design Process</p>
    <h2>From Your Vision to Your Finished Space</h2>
    <p>We follow a structured approach to help organize your interior design journey.</p>
  </div>
  <ol class="process">{process}</ol>
</div>
</section>

<section class="section">
<div class="container">
  <div class="section-head section-head--split">
    <div>
      <p class="eyebrow">Our Projects</p>
      <h2>Explore Our Interior Design Portfolio</h2>
      <p>Every property has its own character, layout, and requirements. Explore our residential, commercial, villa, and apartment interior projects to discover different design concepts and execution examples.</p>
    </div>
    <a class="btn btn--outline" href="{{P}}portfolio.html">View Our Portfolio</a>
  </div>
  <div class="grid grid--4">{port}</div>
</div>
</section>

<section class="section section--white">
<div class="container split split--top">
  <div class="reveal">
    <p class="eyebrow">Visakhapatnam</p>
    <h2>Luxury Interior Designers in Visakhapatnam</h2>
    <div class="divider-rule"></div>
  </div>
  <div class="reveal">
    <p class="lead">Looking for luxury interior designers in Visakhapatnam to transform your home, villa, apartment, or commercial space?</p>
    <p>Vanessa Interiors provides customized interior design and execution services for residential and commercial properties in Vizag.</p>
    <p>From <a class="inline-link" href="{{P}}services/modular-kitchen.html">modular kitchens</a> and <a class="inline-link" href="{{P}}services/bedroom-design.html">bedroom interiors</a> to complete <a class="inline-link" href="{{P}}services/villa-interiors.html">villa interiors</a> and <a class="inline-link" href="{{P}}services/office-interiors.html">office design</a>, our team works to create spaces that combine visual appeal, functionality, and personalized design.</p>
    <p>With 14 years of experience, 100+ completed projects, and a 50+ member team, we help clients explore interior solutions suited to their project requirements.</p>
    <p><strong class="text-ink">Planning your next interior project? Connect with Vanessa Interiors today.</strong></p>
  </div>
</div>
</section>

<section class="section section--tint">
<div class="container grid grid--2 grid--wide-gap">
  <div class="reveal">
    <p class="eyebrow">Testimonials</p>
    <h2>What Our Clients Say</h2>
    <p>Discover feedback from clients who have worked with Vanessa Interiors.</p>
    <div class="review-empty review-empty--inline">
      <span class="quote-mark">“</span>
      <p>We publish only genuine client reviews, shared with our clients' permission. Verified testimonials will appear here soon.</p>
      <a class="link-arrow" href="{{P}}testimonials.html">View All Testimonials {icon("arrow")}</a>
    </div>
  </div>
  <div class="reveal">
    <p class="eyebrow">FAQs</p>
    <h2>Frequently Asked Questions</h2>
    {faq_list(HOME_FAQS)}
    <p class="mt-md"><a class="link-arrow" href="{{P}}faqs.html">View All FAQs {icon("arrow")}</a></p>
  </div>
</div>
</section>

{cta_band("Let's Create Your Dream Space", "Have an interior project in Visakhapatnam or nearby areas? Discuss your requirements with Vanessa Interiors and explore customized luxury interior solutions.")}
'''
    page("index.html", "Luxury Interior Designers in Visakhapatnam | Vanessa Interiors",
         "Vanessa Interiors offers luxury and customized home, villa, office, and commercial interiors in Visakhapatnam. 14 years of experience and 100+ projects.",
         main, active="home", scripts=["calculator"], schema=business_schema())


# ====================================================================== ABOUT
def build_about():
    values = [("Customized Design", "We focus on understanding individual client preferences and project requirements."),
              ("Functional Planning", "We consider how spaces are used when developing interior concepts."),
              ("Design Quality", "We pay attention to design details, materials, finishes, and overall visual consistency."),
              ("Professional Execution", "We coordinate execution work according to the agreed project scope."),
              ("Client Communication", "We aim to maintain clear communication throughout the design and execution process.")]
    facts = [("Established", "2012"), ("Experience", "14 Years"), ("Completed Projects", "100+"), ("Team Size", "50+"),
             ("Location", "Visakhapatnam"), ("Design Focus", "Luxury &amp; Customized"), ("Project Type", "Residential &amp; Commercial")]
    main = page_hero([("Home", "index.html"), ("About Us", None)], "About Us", "About Vanessa Interiors",
                     "Designing interiors with experience &amp; personalization.", art="home-interiors",
                     art_alt="Illustration of an open-plan home interior") + f'''
<section class="section section--white">
<div class="container split split--top">
  <div class="reveal">
    <h2>Designing Interiors with Experience &amp; Personalization</h2>
    <div class="divider-rule"></div>
    <p class="lead">Vanessa Interiors is a luxury and customized interior design company based in Visakhapatnam, Andhra Pradesh.</p>
    <p>Established in 2012, we bring 14 years of experience in interior design and execution, with 100+ completed projects and a team of 50+ members.</p>
    <p>Our services include residential interiors, commercial interiors, modular kitchens, bedrooms, living rooms, wardrobes, false ceilings, villa interiors, renovation, and turnkey interior solutions.</p>
    <p>We believe that every space deserves a design approach that reflects its purpose, personality, and practical requirements.</p>
    <p>Our team works with clients to understand their vision, plan suitable interiors, and coordinate execution according to the agreed project scope.</p>
  </div>
  <div class="panel reveal">
    <p class="eyebrow">Our Experience</p>
    <dl class="facts">{"".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)}</dl>
  </div>
</div>
</section>
<section class="section">
<div class="container">
  <div class="mv-grid">
    <div class="mv-card reveal"><h3>Our Mission</h3><p>To create luxury and customized interiors that combine aesthetics, functionality, and client-specific requirements.</p></div>
    <div class="mv-card reveal"><h3>Our Vision</h3><p>To build Vanessa Interiors into a trusted interior design brand in Visakhapatnam and surrounding markets through thoughtful design, professional execution, and customer-focused service.</p></div>
  </div>
  <div class="section-head mt-xl">
    <p class="eyebrow">Our Core Values</p>
    <h2>What Guides Our Work</h2>
  </div>
  <ol class="value-list">{"".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in values)}</ol>
</div>
</section>
{cta_band("Start Your Interior Project with Vanessa Interiors", "Tell us about your property, design preferences and project scope — our team will help you plan the next step.", primary="Request a Consultation", title_attr="Request a Consultation")}
'''
    page("about.html", "About Vanessa Interiors | Luxury Interior Design Company in Vizag",
         "Learn about Vanessa Interiors, established in 2012, offering luxury and customized residential and commercial interior design services in Visakhapatnam.",
         main, active="about", schema=breadcrumb_schema([("Home", ""), ("About Us", "about.html")]))


# ====================================================================== SERVICES INDEX
def build_services_index():
    residential = ["home-interiors", "modular-kitchen", "bedroom-design", "living-room-design", "wardrobes", "false-ceiling",
                   "villa-interiors", "renovation", "turnkey-interiors"]
    commercial = ["office-interiors", "commercial-interiors", "renovation", "turnkey-interiors"]
    cards = "".join(service_card(s, i + 1) for i, s in enumerate(SERVICES)) + estimator_promo()

    def links(slugs):
        return "".join(f'<li><a href="{{P}}services/{sl}.html">{icon(SERVICE_BY_SLUG[sl]["icon"])} {SERVICE_BY_SLUG[sl]["name"]}</a></li>' for sl in slugs)

    main = page_hero([("Home", "index.html"), ("Services", None)], "Services", "Our Interior Design Services",
                     "Customized interiors for homes, villas &amp; commercial spaces.", wide=True) + f'''
<section class="section section--white section--after-hero">
<div class="container split split--top">
  <div class="reveal">
    <h2>Customized Interiors for Homes, Villas &amp; Commercial Spaces</h2>
    <div class="divider-rule"></div>
    <p>At Vanessa Interiors, we provide interior design and execution services for a variety of residential and commercial properties.</p>
    <p>Our approach combines design planning, personalized solutions, and coordinated execution to help clients create spaces suited to their requirements.</p>
    <p>Whether you need a single-room interior or a complete property transformation, we can discuss your project and develop a suitable scope of work.</p>
  </div>
  <div class="panel panel--tint reveal">
    <p class="eyebrow">Our Service Categories</p>
    <div class="cat-group"><h3>Residential Interior Services</h3><ul class="link-list">{links(residential)}</ul></div>
    <div class="cat-group mt-md"><h3>Commercial Interior Services</h3><ul class="link-list">{links(commercial)}</ul></div>
  </div>
</div>
</section>
<section class="section">
<div class="container">
  <div class="section-head">
    <p class="eyebrow">All Services</p>
    <h2>Choose a Service to Explore</h2>
  </div>
  <div class="grid grid--3">{cards}</div>
</div>
</section>
{cta_band("Discuss Your Interior Requirements", "Share your property details and requirements with our team, or use the cost estimator to plan your budget first.", primary="Get a Quote")}
'''
    page("services.html", "Interior Design Services in Visakhapatnam | Vanessa Interiors",
         "Explore Vanessa Interiors' luxury and customized interior design services in Visakhapatnam, including homes, kitchens, villas, offices, and turnkey projects.",
         main, active="services", schema=breadcrumb_schema([("Home", ""), ("Services", "services.html")]))


# ====================================================================== SERVICE PAGES
def render_block(b, s, idx):
    kind = b[0]
    bg = "section--white" if idx % 2 == 0 else ""
    if kind == "cards":
        _, title, items = b
        cards = ""
        for i, (t, d, link) in enumerate(items):
            more = f'<a class="link-arrow card-link" href="{{P}}services/{link}.html">{SERVICE_BY_SLUG[link]["name"]} {icon("arrow")}</a>' if link and link != s["slug"] else ""
            tint = ["", " icon-tile--green", " icon-tile--blue", " icon-tile--plum"][i % 4]
            cards += f'<div class="card reveal"><span class="icon-tile{tint}">{icon(s["icon"])}</span><h3>{e(t)}</h3><p>{e(d)}</p>{more}</div>'
        cols = "grid--4" if len(items) in (4, 8) else "grid--3"
        return f'''<section class="section {bg}"><div class="container">
<div class="section-head"><p class="eyebrow">{s["name"]}</p><h2>{title}</h2></div>
<div class="grid {cols}">{cards}</div></div></section>'''
    if kind == "checklist":
        _, title, lead, items, note = b
        lead_html = f'<p class="lead">{lead}</p>' if lead else ""
        note_html = f'<p class="note">{note}</p>' if note else ""
        return f'''<section class="section {bg}"><div class="container split split--top">
<div class="reveal"><p class="eyebrow">{s["name"]}</p><h2>{title}</h2><div class="divider-rule"></div>{lead_html}</div>
<div class="panel reveal"><ul class="checklist{" checklist--2" if len(items) > 5 else ""}">{"".join(f"<li>{e(x)}</li>" for x in items)}</ul>{note_html}</div>
</div></section>'''
    if kind == "text":
        _, title, paras = b
        return f'''<section class="section {bg}"><div class="container split split--top">
<div class="reveal"><p class="eyebrow">{s["name"]}</p><h2>{title}</h2><div class="divider-rule"></div></div>
<div class="reveal">{"".join(f'<p class="lead">{e(x)}</p>' for x in paras)}</div></div></section>'''
    if kind == "chain":
        _, title, items, note = b
        note_html = f'<p class="note note--narrow">{note}</p>' if note else ""
        return f'''<section class="section {bg}"><div class="container">
<div class="section-head"><p class="eyebrow">Process</p><h2>{title}</h2></div>
<ol class="chain reveal">{"".join(f"<li>{e(x)}</li>" for x in items)}</ol>{note_html}</div></section>'''
    if kind == "steps":
        _, title, items = b
        lis = ""
        for i, (t, d) in enumerate(items):
            label, heading = (t, "") if t.startswith("Step") else (f"Step {i + 1}", f"<h3>{e(t)}</h3>")
            lis += f'<li class="reveal"><span class="process__step">{label}</span>{heading}<p>{e(d)}</p></li>'
        return f'''<section class="section section--dark"><div class="container">
<div class="section-head"><p class="eyebrow eyebrow--light">Process</p><h2>{title}</h2></div>
<ol class="process">{lis}</ol></div></section>'''
    raise ValueError(kind)


def build_service(s):
    name = s["name"]
    est_btn = (f'<a class="btn btn--ghost" href="{{P}}cost-estimator.html?type={s["est"]}">{icon("calc")} Estimate Cost</a>'
               if s.get("est") else "")
    hero_extra = f'''<div class="btn-row mt-md">
  <button type="button" class="btn btn--primary" data-lead="{e(name)}">Get a Quote</button>
  <a class="btn btn--whatsapp" href="{WA_URL}" data-whatsapp="{e(name)}">{icon("whatsapp")} WhatsApp About {name}</a>
  {est_btn}
</div>'''
    main = page_hero([("Home", "index.html"), ("Services", "services.html"), (name, None)],
                     f"{name} · Visakhapatnam", s["h1"], e(s["intro"][0]), hero_extra,
                     art=s["img"], art_alt=f"{name} design illustration")

    # introduction
    rest = "".join(f"<p class=\"lead\">{e(x)}</p>" for x in s["intro"][1:])
    link_html = ""
    if s.get("link_sentence"):
        sentence, target = s["link_sentence"]
        pre, _, post = sentence.partition("{")
        anchor, _, tail = post.partition("}")
        link_html = f'<p>{pre}<a class="inline-link" href="{{P}}services/{target}.html">{anchor}</a>{tail}</p>'
    main += f'''<section class="section section--white"><div class="container split split--top">
<div class="reveal">{rest}{link_html}</div>
<div class="panel panel--tint reveal">
  <p class="eyebrow">Why Vanessa Interiors</p>
  <dl class="facts">
    <div><dt>Experience</dt><dd>14 Years</dd></div>
    <div><dt>Completed Projects</dt><dd>100+</dd></div>
    <div><dt>Team</dt><dd>50+ Members</dd></div>
    <div><dt>Execution</dt><dd>Own Workers</dd></div>
    <div><dt>Projects Start From</dt><dd>₹5 Lakhs</dd></div>
  </dl>
</div></div></section>'''

    for i, b in enumerate(s["blocks"]):
        main += render_block(b, s, i + 1)

    # project images / real work pointer
    main += f'''<section class="section section--tint section--tight"><div class="container">
<div class="coming-soon reveal">
  <span class="icon-tile">{icon("grid")}</span>
  <div><h3>See Our {name} Work</h3><p>Browse genuine project photographs in our portfolio and gallery, or ask us on WhatsApp for recent {name.lower()} projects.</p>
  <div class="btn-row mt-sm"><a class="btn btn--outline btn--sm" href="{{P}}portfolio.html">View Portfolio</a><a class="btn btn--ghost btn--sm" href="{{P}}gallery.html">Open Gallery</a></div></div>
</div></div></section>'''

    # FAQ
    faq_pairs = [FAQS[i] for i in s["faq"]]
    main += f'''<section class="section section--white"><div class="container split split--top">
<div class="reveal"><p class="eyebrow">FAQs</p><h2>Questions About {name}</h2><div class="divider-rule"></div><a class="link-arrow" href="{{P}}faqs.html">View All FAQs {icon("arrow")}</a></div>
<div class="reveal">{faq_list(faq_pairs)}</div></div></section>'''

    # CTA
    main += cta_band(s["cta"], f"Discuss your {name.lower()} requirements with Vanessa Interiors — share your property details and preferences, and our team will help plan a suitable scope.",
                     service=name, primary="Get a Quote")

    # related
    rel = "".join(service_mini(SERVICE_BY_SLUG[r]) for r in s["related"])
    main += f'''<section class="section section--pt-sm"><div class="container">
<div class="section-head section-head--split"><div><p class="eyebrow">Related Services</p><h2>Explore Related Services</h2></div>
<a class="btn btn--outline" href="{{P}}services.html">← Back to All Services</a></div>
<div class="grid {"grid--3" if len(s["related"]) == 3 else "grid--2"}">{rel}</div></div></section>'''

    faq_schema = {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": name,
                  "areaServed": "Visakhapatnam", "provider": {"@type": "HomeAndConstructionBusiness", "name": "Vanessa Interiors", "url": SITE_URL},
                  "description": s["meta_desc"]}
    page(f"services/{s['slug']}.html", s["meta_title"], s["meta_desc"], main, active="services", service_slug=s["slug"],
         schema=[faq_schema, breadcrumb_schema([("Home", ""), ("Services", "services.html"), (name, f"services/{s['slug']}.html")])],
         lead_service=name)


# ====================================================================== ESTIMATOR PAGE
def build_estimator_page():
    main = page_hero([("Home", "index.html"), ("Cost Estimator", None)], "Interior Cost Estimator",
                     "Estimate Your Interior Cost", "Choose what you'd like to estimate, enter your area in sq.ft., and get an instant planning estimate. Discuss it with our team on WhatsApp in one tap.", wide=True) + f'''
<section class="section pt-0">
<div class="container">{estimator("h2")}</div>
</section>
<section class="section section--white section--tight">
<div class="container split split--top">
  <div><p class="eyebrow">Planning Your Budget</p><h2>What Affects the Final Cost?</h2><div class="divider-rule"></div></div>
  <div>
    <p>{DISCLAIMER}</p>
    <p>Our projects start from ₹5 Lakhs. For an accurate, itemised quotation, our team reviews your layout, requirements and preferred materials during consultation.</p>
    <div class="btn-row mt-md">
      <button type="button" class="btn btn--primary" data-lead="General Enquiry" data-lead-title="Book Site Visit">Book Site Visit</button>
      <a class="btn btn--whatsapp" href="{WA_URL}" data-whatsapp="Interior Cost Estimate">{icon("whatsapp")} WhatsApp Us</a>
    </div>
  </div>
</div>
</section>'''
    page("cost-estimator.html", "Interior Cost Estimator Visakhapatnam | Vanessa Interiors",
         "Estimate your interior cost instantly with the Vanessa Interiors cost estimator — complete home, kitchen, wardrobes, bedroom and living area.",
         main, scripts=["calculator"], schema=breadcrumb_schema([("Home", ""), ("Cost Estimator", "cost-estimator.html")]))


# ====================================================================== PORTFOLIO
def build_portfolio():
    cards = "".join(f'''<a class="cat-card card--hover reveal" href="{{P}}portfolio/{c["slug"]}.html">
<img src="{{P}}images/services/{c["img"]}.svg" alt="{c["name"]} interiors illustration" loading="lazy" width="800" height="600">
<div class="cat-card__body"><h3>{c["name"]}</h3><p>{c["card"]}</p><span class="link-arrow">Explore {c["name"].lower()} {icon("arrow")}</span></div></a>''' for c in PORTFOLIO)
    main = page_hero([("Home", "index.html"), ("Portfolio", None)], "Portfolio", "Our Interior Design Portfolio",
                     "Explore our design &amp; execution work.", wide=True) + f'''
<section class="section section--white section--after-hero">
<div class="container">
  <div class="section-head">
    <h2>Explore Our Design &amp; Execution Work</h2>
    <p>Every project reflects different requirements, design preferences, and property layouts.</p>
    <p>Our portfolio showcases interior design work across residential and commercial spaces, helping visitors explore our design approach, materials, layouts, and finishes.</p>
    <p>Browse our project categories to discover inspiration for your next interior project.</p>
  </div>
  <div class="grid grid--4">{cards}</div>
  <div class="project-grid mt-lg" data-portfolio-list="all">
    <div class="coming-soon"><span class="icon-tile icon-tile--blue">{icon("grid")}</span>
    <div><h3>Project photographs are being curated</h3><p>We're adding genuine photographs and details of our completed projects. Want to see recent work now? Ask us on WhatsApp.</p></div></div>
  </div>
</div>
</section>
{cta_band("Explore Our Projects", "Ask our team for recent project photographs relevant to your home, villa, office or commercial space.", primary="Request a Consultation", title_attr="Request a Consultation")}'''
    page("portfolio.html", "Interior Design Portfolio in Visakhapatnam | Vanessa Interiors",
         "Explore Vanessa Interiors' residential, commercial, villa, and apartment interior design projects in Visakhapatnam.",
         main, active="portfolio", scripts=["portfolio"], schema=breadcrumb_schema([("Home", ""), ("Portfolio", "portfolio.html")]))

    for c in PORTFOLIO:
        others = "".join(f'<li><a href="{{P}}portfolio/{o["slug"]}.html">{o["name"]}</a></li>' for o in PORTFOLIO if o is not c)
        main = page_hero([("Home", "index.html"), ("Portfolio", "portfolio.html"), (c["name"], None)], f"Portfolio · {c['name']}",
                         c["h1"], c["h2"], art=c["img"], art_alt=f"{c['name']} interiors illustration") + f'''
<section class="section section--white">
<div class="container split split--top">
  <div class="reveal">
    <h2>{c["h2"]}</h2><div class="divider-rule"></div>
    {"".join(f"<p>{x}</p>" for x in c["intro"])}
  </div>
  <div class="panel panel--tint reveal">
    <p class="eyebrow">Project Categories</p>
    <ul class="pill-list">{"".join(f"<li>{x}</li>" for x in c["cats"])}</ul>
  </div>
</div>
</section>
<section class="section">
<div class="container">
  <div class="section-head"><p class="eyebrow">Projects</p><h2>{c["name"]} Projects</h2></div>
  <div class="project-grid" data-portfolio-list="{c["slug"]}">
    <div class="coming-soon"><span class="icon-tile">{icon("grid")}</span>
    <div><h3>Verified project details coming soon</h3><p>We're adding genuine {c["name"].lower()} project photographs with accurate details. Ask us on WhatsApp to see recent work.</p>
    <div class="btn-row mt-sm"><a class="btn btn--whatsapp btn--sm" href="{WA_URL}" data-whatsapp="{c["service"]}">{icon("whatsapp")} WhatsApp Us</a></div></div></div>
  </div>
  <div class="mt-lg"><p class="eyebrow">More Categories</p><ul class="link-list">{others}<li><a href="{{P}}portfolio.html">All Portfolio</a></li></ul></div>
</div>
</section>
{cta_band(c["cta"], "Share your property details and design preferences with our team to begin planning.", service=c["service"], primary="Get a Quote")}'''
        page(f"portfolio/{c['slug']}.html", c["meta_title"], c["meta_desc"], main, active="portfolio", scripts=["portfolio"],
             schema=breadcrumb_schema([("Home", ""), ("Portfolio", "portfolio.html"), (c["name"], f"portfolio/{c['slug']}.html")]),
             lead_service=c["service"])


# ====================================================================== GALLERY
def build_gallery():
    main = page_hero([("Home", "index.html"), ("Gallery", None)], "Gallery", "Interior Design Inspiration Gallery",
                     "Explore our design details.", wide=True) + f'''
<section class="section section--white section--after-hero">
<div class="container">
  <div class="section-head">
    <h2>Explore Our Design Details</h2>
    <p>Discover interior design ideas and project photographs showcasing different styles, materials, furniture concepts, and design elements.</p>
    <p>Our gallery helps you explore possible ideas for your home, villa, office, or commercial property.</p>
  </div>
  <div class="chip-row gallery-filters" id="galleryFilters" role="group" aria-label="Filter gallery"></div>
  <div class="gallery-grid" id="galleryGrid"></div>
</div>
</section>
{cta_band("Discuss Your Design Ideas", "Found a style you like? Share it with our team and we'll help you plan it for your space.", primary="Enquire Now", title_attr="Enquire Now")}'''
    page("gallery.html", "Interior Design Gallery in Visakhapatnam | Vanessa Interiors",
         "Browse the Vanessa Interiors gallery for home interiors, modular kitchens, bedrooms, living rooms, villas, offices, and commercial spaces.",
         main, active="gallery", scripts=["gallery"], schema=breadcrumb_schema([("Home", ""), ("Gallery", "gallery.html")]))


# ====================================================================== BLOG
def build_blog():
    cats = "".join(f"<li>{c}</li>" for c in BLOG_CATEGORIES)
    cards = "".join(f'''<article class="blog-card reveal">
<span class="tag">{cat}</span><h3>{t}</h3><p>Focus: {kw}</p><span class="tag tag--soon">Article coming soon</span>
<a class="link-arrow" href="{{P}}{href}">Related: {label} {icon("arrow")}</a></article>''' for t, kw, cat, href, label in BLOG_TOPICS)
    main = page_hero([("Home", "index.html"), ("Blog", None)], "Blog", "Interior Design Ideas &amp; Inspiration",
                     "Expert insights for your next interior project.", wide=True) + f'''
<section class="section section--white section--after-hero">
<div class="container split split--top">
  <div class="reveal">
    <h2>Expert Insights for Your Next Interior Project</h2><div class="divider-rule"></div>
    <p>Planning a new home interior, renovating your space, or designing a commercial property?</p>
    <p>Our blog provides helpful information about interior design, space planning, materials, renovation, and project considerations.</p>
    <p>Explore practical ideas and guidance to help you make informed decisions for your interior project.</p>
  </div>
  <div class="panel panel--tint reveal"><p class="eyebrow">Blog Categories</p><ul class="pill-list">{cats}</ul></div>
</div>
</section>
<section class="section">
<div class="container">
  <div class="section-head"><p class="eyebrow">Upcoming Articles</p><h2>Topics We're Writing About</h2>
  <p>In-depth guides are on the way. Meanwhile, each topic links to the related service or tool.</p></div>
  <div class="grid grid--3">{cards}</div>
</div>
</section>
{cta_band("Need Professional Interior Design? Contact Vanessa Interiors", "Talk to our team about your home, villa, office or commercial interior project.", primary="Contact Us", title_attr="Contact Us")}'''
    page("blog.html", "Interior Design Blog in Visakhapatnam | Vanessa Interiors",
         "Explore interior design tips, home decor ideas, modular kitchen guides, renovation advice, and luxury interior inspiration from Vanessa Interiors.",
         main, active="blog", schema=breadcrumb_schema([("Home", ""), ("Blog", "blog.html")]))


# ====================================================================== CONTACT
def build_contact():
    prop = ["Apartment", "Independent House", "Villa", "Office", "Commercial Space", "Other"]
    budget = ["₹5–10 Lakhs", "₹10–20 Lakhs", "₹20–40 Lakhs", "₹40 Lakhs+", "Discuss with Team"]
    svc_opts = "".join(f'<option value="{e(s["name"])}">{s["name"]}</option>' for s in SERVICES)
    map_q = "Aruna+Inn,+Sankara+Matam+Road,+Madhuranagar,+Akkayyapalem,+Visakhapatnam+530016"
    main = page_hero([("Home", "index.html"), ("Contact Us", None)], "Contact Us", "Let's Discuss Your Interior Design Project",
                     "Your dream space starts with a conversation.", wide=True) + f'''
<section class="section section--white section--after-hero">
<div class="container contact-grid">
  <div class="reveal">
    <h2>Your Dream Space Starts with a Conversation</h2>
    <div class="divider-rule"></div>
    <p>Planning a new home interior, renovating your existing property, or designing a commercial space?</p>
    <p>Vanessa Interiors is here to discuss your requirements and explore customized interior design solutions.</p>
    <p>Contact us to discuss your property, design preferences, project scope, and budget.</p>
    <ul class="contact-list mt-md">
      <li><span class="icon-tile">{icon("pin")}</span><div><strong>Office Address</strong><span>{ADDRESS}</span></div></li>
      <li><span class="icon-tile icon-tile--green">{icon("phone")}</span><div><strong>Phone</strong><a href="tel:{PHONE_LINK}" data-phone-link>{PHONE}</a></div></li>
      <li><span class="icon-tile icon-tile--blue">{icon("mail")}</span><div><strong>Email</strong><a href="mailto:{EMAIL}" data-email-link>{EMAIL}</a></div></li>
      <li><span class="icon-tile icon-tile--plum">{icon("globe")}</span><div><strong>Website</strong><a href="{SITE_URL}">www.vanessainteriors.in</a></div></li>
      <li><span class="icon-tile">{icon("instagram")}</span><div><strong>Instagram</strong><a href="{INSTAGRAM}" target="_blank" rel="noopener">@vanessainteriorsindia</a></div></li>
    </ul>
    <div class="btn-row">
      <a class="btn btn--whatsapp" href="{WA_URL}" data-whatsapp="">{icon("whatsapp")} WhatsApp Us</a>
      <a class="btn btn--outline" href="tel:{PHONE_LINK}" data-phone-link>{icon("phone")} Call Us Today</a>
    </div>
  </div>
  <div class="panel reveal">
    <h2 class="h2-sm">Request a Consultation</h2>
    <form id="contactForm" novalidate>
      <div class="field-row">
        <div class="field"><label for="cName">Full Name <span class="req">*</span></label><input id="cName" name="name" type="text" autocomplete="name" required><p class="field__error" data-error-for="name"></p></div>
        <div class="field"><label for="cPhone">Phone Number <span class="req">*</span></label><input id="cPhone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required><p class="field__error" data-error-for="phone"></p></div>
      </div>
      <div class="field"><label for="cEmail">Email Address</label><input id="cEmail" name="email" type="email" autocomplete="email"><p class="field__error" data-error-for="email"></p></div>
      <div class="field-row">
        <div class="field"><label for="cProp">Property Type</label><select id="cProp" name="propertyType"><option value="">Select</option>{"".join(f"<option>{x}</option>" for x in prop)}</select></div>
        <div class="field"><label for="cLoc">Project Location</label><input id="cLoc" name="location" type="text"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="cSvc">Preferred Service</label><select id="cSvc" name="service"><option value="">Select</option>{svc_opts}</select></div>
        <div class="field"><label for="cBudget">Estimated Budget</label><select id="cBudget" name="budget"><option value="">Select</option>{"".join(f"<option>{x}</option>" for x in budget)}</select></div>
      </div>
      <div class="field"><label for="cMsg">Message</label><textarea id="cMsg" name="message" rows="4"></textarea></div>
      <button type="submit" class="btn btn--primary btn--block">Submit Your Inquiry</button>
      <p class="form-status" id="contactStatus" role="status" aria-live="polite"></p>
    </form>
  </div>
</div>
</section>
<section class="section">
<div class="container split">
  <div class="reveal">
    <p class="eyebrow">Visakhapatnam</p>
    <h2>Visit Vanessa Interiors in Visakhapatnam</h2>
    <div class="divider-rule"></div>
    <p>Looking for a luxury and customized interior design company in Visakhapatnam?</p>
    <p>Vanessa Interiors provides residential and commercial interior design solutions for homes, apartments, villas, offices, and commercial properties.</p>
    <p>Our office is located on Sankara Matam Road, Madhuranagar, Akkayyapalem, Visakhapatnam.</p>
    <p>Contact our team to discuss your interior design requirements.</p>
    <a class="btn btn--primary" href="tel:{PHONE_LINK}" data-phone-link>{icon("phone")} Call Us Today</a>
  </div>
  <div class="map-embed reveal">
    <iframe title="Vanessa Interiors office location on Google Maps" src="https://www.google.com/maps?q={map_q}&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</div>
</section>'''
    page("contact.html", "Contact Vanessa Interiors | Interior Designers in Visakhapatnam",
         "Contact Vanessa Interiors for luxury home interiors, modular kitchens, villa interiors, office design, and turnkey interior services in Visakhapatnam.",
         main, active="contact", schema=[business_schema(), breadcrumb_schema([("Home", ""), ("Contact Us", "contact.html")])])


# ====================================================================== FAQ / TESTIMONIALS / LEGAL / 404
def build_faqs():
    pairs = [FAQS[i] for i in sorted(FAQS)]
    schema = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}
    main = page_hero([("Home", "index.html"), ("FAQs", None)], "FAQs", "Frequently Asked Questions",
                     "Answers to common questions about our home interiors, modular kitchens, villa interiors, commercial projects and turnkey services.", wide=True) + f'''
<section class="section section--white section--after-hero">
<div class="container container--narrow">
{faq_list(pairs)}
<div class="panel panel--tint mt-lg center">
  <h3>Still have a question?</h3>
  <p class="muted">Call us on <a href="tel:{PHONE_LINK}" data-phone-link>{PHONE}</a> or send a message on WhatsApp.</p>
  <div class="btn-row btn-row--center"><a class="btn btn--whatsapp" href="{WA_URL}" data-whatsapp="">{icon("whatsapp")} WhatsApp Us</a><button type="button" class="btn btn--primary" data-lead="General Enquiry" data-lead-title="Enquire Now">Enquire Now</button></div>
</div>
</div>
</section>'''
    page("faqs.html", "FAQs | Vanessa Interiors Interior Design Services in Visakhapatnam",
         "Find answers to common questions about Vanessa Interiors' home interiors, modular kitchens, villa interiors, commercial projects, and turnkey services.",
         main, schema=schema)


def build_testimonials():
    main = page_hero([("Home", "index.html"), ("Testimonials", None)], "Testimonials", "What Our Clients Say",
                     "Real experiences. Real projects.", wide=True) + f'''
<section class="section section--white section--after-hero">
<div class="container">
  <div class="section-head section-head--center">
    <h2>Real Experiences. Real Projects.</h2>
    <p>We value the feedback and experiences of our clients.</p>
    <p>Explore genuine testimonials from customers who have worked with Vanessa Interiors on their interior design and execution projects.</p>
  </div>
  <!--
    TESTIMONIAL TEMPLATE — publish only verified reviews with the client's permission.
    <article class="card">
      <p>"[Verified Customer Feedback]"</p>
      <h3>[Actual Client Name]</h3>
      <p class="muted">[Apartment / Villa / Office] · [Project Location]</p>
    </article>
  -->
  <div class="review-empty reveal">
    <span class="quote-mark">“</span>
    <h3>Verified client reviews coming soon</h3>
    <p>We only publish genuine feedback, shared with our clients' permission. Reviews are being collected and will appear here.</p>
  </div>
</div>
</section>
{cta_band("Discuss Your Project with Our Team", "Tell us about your space and requirements — we'll help you plan the next step.", primary="Request a Consultation", title_attr="Request a Consultation")}'''
    page("testimonials.html", "Client Testimonials | Vanessa Interiors Visakhapatnam",
         "Read genuine customer testimonials about Vanessa Interiors' residential and commercial interior design and execution services in Visakhapatnam.",
         main)


def legal(path, title, h1, sections, intro):
    body = "".join(intro)
    for h, paras, items in sections:
        body += f"<h2>{h}</h2>" + "".join(f"<p>{x}</p>" for x in paras)
        if items:
            body += "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
    body += f'''<h2>Contact Us</h2><p><strong>Vanessa Interiors</strong><br>Email: <a href="mailto:{EMAIL}" data-email-link>{EMAIL}</a><br>Phone: <a href="tel:{PHONE_LINK}" data-phone-link>{PHONE}</a></p>'''
    main = page_hero([("Home", "index.html"), (h1, None)], "Legal", h1, "Effective Date: [Insert Date]", wide=True) + f'''
<section class="section section--white section--after-hero"><div class="container"><div class="prose">{body}</div></div></section>'''
    page(path, title, f"{h1} for the Vanessa Interiors website.", main)


def build_legal():
    legal("privacy-policy.html", "Privacy Policy | Vanessa Interiors", "Privacy Policy", [
        ("1. Information We Collect", ["Depending on the features of our website, we may collect information such as:"],
         ["Name", "Phone number", "Email address", "Project location", "Property details", "Interior design requirements", "Other information submitted through contact forms"]),
        ("2. How We Use Your Information", ["We may use the information you provide to:"],
         ["Respond to inquiries", "Discuss your interior design requirements", "Schedule consultations", "Provide requested information", "Coordinate relevant services", "Improve our website and customer experience"]),
        ("3. Information Sharing", ["Information may be shared with relevant service providers where necessary for legitimate business operations, legal obligations, or other disclosed purposes."], []),
        ("4. Data Security", ["We take reasonable steps to protect personal information. However, no online system can guarantee complete security."], []),
        ("5. Cookies", ["Our website may use cookies or similar technologies, depending on its configuration."], []),
        ("6. Your Rights and Choices", ["Depending on applicable law, you may have rights concerning your personal information, including requesting access, correction, or deletion where applicable."], []),
    ], ["<p>Vanessa Interiors respects your privacy and is committed to protecting the information you provide through our website.</p>",
        "<p>This policy explains how we may collect, use, and handle personal information submitted through our website.</p>"])
    legal("terms.html", "Terms & Conditions | Vanessa Interiors", "Terms &amp; Conditions", [
        ("1. Website Information", ["The information on this website is provided for general business and service-related purposes."], []),
        ("2. Services", ["Vanessa Interiors offers interior design and execution services according to the specific requirements and agreed scope of each project."], []),
        ("3. Project Scope", ["Design concepts, materials, execution responsibilities, pricing, timelines, and deliverables are subject to the project agreement."], []),
        ("4. Pricing &amp; Estimates", ["Any estimate or price discussed during consultations may be subject to changes based on design modifications, materials, specifications, and finalized scope.",
                                        "Results from the online Interior Cost Estimator are for initial planning purposes only and are not a quotation."], []),
        ("5. Payments", ["Payment schedules, advance requirements, and other commercial terms are defined in the applicable project agreement."], []),
        ("6. Project Timelines", ["Project timelines depend on scope, materials, site conditions, approvals, and other relevant factors."], []),
        ("7. Intellectual Property", ["Website content, branding, photographs, and other materials may be protected by applicable intellectual property laws."], []),
        ("8. External Links", ["The website may contain links to external websites. Vanessa Interiors is not responsible for third-party content or policies."], []),
        ("9. Changes to Terms", ["We may update these terms when necessary. Changes will be published with the applicable effective date."], []),
    ], ["<p>These terms and conditions apply to the use of the Vanessa Interiors website.</p>"])


def build_404():
    main = f'''<section class="section error-page"><div class="container">
<p class="code">404</p><h1 class="h1-sm">This page could not be found</h1>
<p class="lead">The page may have moved. Try one of these instead:</p>
<ul class="link-list link-list--center"><li><a href="{{P}}index.html">Home</a></li><li><a href="{{P}}services.html">Services</a></li><li><a href="{{P}}cost-estimator.html">Cost Estimator</a></li><li><a href="{{P}}contact.html">Contact</a></li></ul>
</div></section>'''
    page("404.html", "Page Not Found | Vanessa Interiors", "The page you are looking for could not be found.", main, root="/")


# ====================================================================== RUN
if __name__ == "__main__":
    build_home()
    build_about()
    build_services_index()
    for s in SERVICES:
        build_service(s)
    build_estimator_page()
    build_portfolio()
    build_gallery()
    build_blog()
    build_contact()
    build_faqs()
    build_testimonials()
    build_legal()
    build_404()
    for path, html in PAGES.items():
        full = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(html)
    print(len(PAGES), "pages written")
