/* =========================================================
   MAIN — navigation, CTA wiring, small UI behaviours.
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {
    initHeader();
    initNavigation();
    initCtaDelegation();
    initContactLinks();
    const year = document.querySelectorAll("[data-year]");
    year.forEach(function (el) { el.textContent = new Date().getFullYear(); });
});

/* Header shadow once the page scrolls */
function initHeader() {
    const header = document.querySelector(".site-header");
    if (!header) return;
    const onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
}

/* Mobile menu + Services dropdown (hover on desktop via CSS, click/tap everywhere) */
function initNavigation() {
    const toggle = document.querySelector(".nav-toggle");
    const nav = document.getElementById("siteNav");
    if (toggle && nav) {
        toggle.addEventListener("click", function () {
            const open = toggle.getAttribute("aria-expanded") === "true";
            toggle.setAttribute("aria-expanded", String(!open));
            nav.classList.toggle("is-open", !open);
            document.body.classList.toggle("nav-open", !open);
        });
    }

    
    document.querySelectorAll(".has-dropdown > .dropdown-toggle").forEach(function (btn) {
        btn.addEventListener("click", function () {
            const item = btn.parentElement;
            const open = btn.getAttribute("aria-expanded") === "true";
            btn.setAttribute("aria-expanded", String(!open));
            item.classList.toggle("is-open", !open);
        });
    });

    // close dropdown / menu with Escape or outside click
    document.addEventListener("keydown", function (ev) {
        if (ev.key !== "Escape") return;
        document.querySelectorAll(".has-dropdown.is-open").forEach(closeDropdown);
        if (nav && nav.classList.contains("is-open") && toggle) toggle.click();
    });
    document.addEventListener("click", function (ev) {
        document.querySelectorAll(".has-dropdown.is-open").forEach(function (item) {
            if (!item.contains(ev.target) && window.innerWidth > 1080) closeDropdown(item);
        });
    });
}

function closeDropdown(item) {
    item.classList.remove("is-open");
    const btn = item.querySelector(".dropdown-toggle");
    if (btn) btn.setAttribute("aria-expanded", "false");
}

/* One listener handles every CTA on every page:
   data-lead="Service"            -> openLeadPopup(Service)
   data-lead-title="Book Site Visit" (optional popup heading)
   data-whatsapp="Service"        -> openWhatsApp(Service)
   data-whatsapp-estimate         -> openEstimateWhatsApp()          */
   
function initCtaDelegation() {
    document.addEventListener("click", function (ev) {
        const lead = ev.target.closest("[data-lead]");
        if (lead) {
            ev.preventDefault();
            const opts = { title: lead.getAttribute("data-lead-title") || "" };
            openLeadPopup(lead.getAttribute("data-lead"), opts);
            return;
        }
        const est = ev.target.closest("[data-whatsapp-estimate]");
        if (est) {
            ev.preventDefault();
            openEstimateWhatsApp();
            return;
        }
        const wa = ev.target.closest("[data-whatsapp]");
        if (wa) {
            ev.preventDefault();
            openWhatsApp(wa.getAttribute("data-whatsapp"));
        }
    });
}



/* Fills phone / email / address from SITE_CONFIG so they are set in one place */
function initContactLinks() {
    document.querySelectorAll("[data-phone-link]").forEach(function (a) { a.href = "tel:" + SITE_CONFIG.phoneLink; });
    document.querySelectorAll("[data-phone-text]").forEach(function (el) { el.textContent = SITE_CONFIG.phone; });
    document.querySelectorAll("[data-email-link]").forEach(function (a) { a.href = "mailto:" + SITE_CONFIG.email; });
    document.querySelectorAll("[data-email-text]").forEach(function (el) { el.textContent = SITE_CONFIG.email; });
}

/* Scroll reveals and other motion live in js/animations.js */
