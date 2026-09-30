/* =========================================================
   LEAD POPUP — one compact popup for every quote/enquiry CTA.
   Buttons use:  data-lead="Modular Kitchen"
                 data-lead-title="Book Site Visit"   (optional)
   Or call directly: openLeadPopup("Modular Kitchen");
   ========================================================= */

let leadPopupLastFocus = null;
let leadPopupService = "";

function buildLeadPopup() {
    if (document.getElementById("leadModal")) return;

    const wrapper = document.createElement("div");
    wrapper.innerHTML =
        '<div class="lead-modal" id="leadModal" hidden>' +
          '<div class="lead-modal__backdrop" data-close-lead></div>' +
          '<div class="lead-modal__dialog" role="dialog" aria-modal="true" aria-labelledby="leadTitle">' +
            '<button type="button" class="lead-modal__close" data-close-lead aria-label="Close">' +
              '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>' +
            '</button>' +
            '<div class="lead-modal__head">' +
              '<span class="lead-modal__rule"></span>' +
              '<h2 id="leadTitle" class="lead-modal__title">Get a Quote</h2>' +
            '</div>' +
            '<form class="lead-form" id="leadForm" novalidate>' +
              '<div class="field">' +
                '<label for="leadService">Interested Service</label>' +
                '<select id="leadService" name="service"></select>' +
              '</div>' +
              '<div class="field">' +
                '<label for="leadName">Name <span class="req">*</span></label>' +
                '<input id="leadName" name="name" type="text" autocomplete="name" required>' +
                '<p class="field__error" data-error-for="name"></p>' +
              '</div>' +
              '<div class="field-row">' +
                '<div class="field">' +
                  '<label for="leadPhone">Phone <span class="req">*</span></label>' +
                  '<input id="leadPhone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required>' +
                  '<p class="field__error" data-error-for="phone"></p>' +
                '</div>' +
                '<div class="field">' +
                  '<label for="leadWhatsapp">WhatsApp Number</label>' +
                  '<input id="leadWhatsapp" name="whatsapp" type="tel" inputmode="tel">' +
                  '<p class="field__error" data-error-for="whatsapp"></p>' +
                '</div>' +
              '</div>' +
              '<div class="field-row">' +
                '<div class="field">' +
                  '<label for="leadArea">Area (Sq.Ft.)</label>' +
                  '<input id="leadArea" name="area" type="text" inputmode="decimal">' +
                  '<p class="field__error" data-error-for="area"></p>' +
                '</div>' +
                '<div class="field">' +
                  '<label for="leadLocation">Project Location</label>' +
                  '<input id="leadLocation" name="location" type="text" autocomplete="address-level2">' +
                '</div>' +
              '</div>' +
              '<button type="submit" class="btn btn--primary btn--block">Submit Enquiry</button>' +
              '<button type="button" class="btn btn--whatsapp btn--block" id="leadWhatsappBtn">' +
                '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-whatsapp"></use></svg> WhatsApp Us' +
              '</button>' +
            '</form>' +
            '<div class="lead-modal__success" id="leadSuccess" hidden>' +
              '<div class="success-mark" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div>' +
              '<h3>Thank you!</h3>' +
              '<p id="leadSuccessText">Our team will contact you shortly.</p>' +
              '<button type="button" class="btn btn--ghost btn--block" data-close-lead>Close</button>' +
            '</div>' +
          '</div>' +
        '</div>';
    document.body.appendChild(wrapper.firstChild);

    // service options: services + estimator categories + general
    const select = document.getElementById("leadService");
    const options = SERVICES.concat(Object.values(INTERIOR_TYPES), ["General Enquiry"]);
    Array.from(new Set(options)).forEach(function (name) {
        const opt = document.createElement("option");
        opt.value = name;
        opt.textContent = name;
        select.appendChild(opt);
    });
    select.addEventListener("change", function () { leadPopupService = select.value; });

    const modal = document.getElementById("leadModal");
    modal.addEventListener("click", function (ev) {
        if (ev.target.closest("[data-close-lead]")) closeLeadPopup();
    });
    modal.addEventListener("keydown", trapLeadFocus);
    document.getElementById("leadWhatsappBtn").addEventListener("click", function () {
        openWhatsApp(leadPopupService === "General Enquiry" ? "" : leadPopupService);
    });
    document.getElementById("leadForm").addEventListener("submit", handleLeadSubmit); // forms.js
}

function openLeadPopup(serviceName, options) {
    buildLeadPopup();
    const opts = options || {};
    const modal = document.getElementById("leadModal");
    const form = document.getElementById("leadForm");
    const select = document.getElementById("leadService");
    const name = (serviceName || "General Enquiry").trim();

    // make sure the service exists in the list, then select it
    if (!Array.from(select.options).some(function (o) { return o.value === name; })) {
        const opt = document.createElement("option");
        opt.value = name;
        opt.textContent = name;
        select.insertBefore(opt, select.firstChild);
    }
    select.value = name;
    leadPopupService = name;

    document.getElementById("leadTitle").textContent = opts.title || "Get a Quote";
    form.hidden = false;
    document.getElementById("leadSuccess").hidden = true;
    clearFormErrors(form); // forms.js

    // pre-fill area from the estimator when available
    const areaInput = document.getElementById("leadArea");
    if (opts.area) {
        areaInput.value = opts.area;
    } else if (window.lastEstimate && !areaInput.value) {
        areaInput.value = window.lastEstimate.area;
    }

    leadPopupLastFocus = document.activeElement;
    modal.hidden = false;
    document.body.classList.add("modal-open");
    requestAnimationFrame(function () {
        modal.classList.add("is-open");
        document.getElementById("leadName").focus();
    });
}

function closeLeadPopup() {
    const modal = document.getElementById("leadModal");
    if (!modal || modal.hidden) return;
    modal.classList.remove("is-open");
    document.body.classList.remove("modal-open");
    setTimeout(function () { modal.hidden = true; }, 200);
    if (leadPopupLastFocus && leadPopupLastFocus.focus) leadPopupLastFocus.focus();
}

function trapLeadFocus(ev) {
    if (ev.key === "Escape") {
        closeLeadPopup();
        return;
    }
    if (ev.key !== "Tab") return;
    const dialog = document.querySelector(".lead-modal__dialog");
    const focusable = Array.from(dialog.querySelectorAll("button, input, select, textarea, a[href]"))
        .filter(function (el) { return el.offsetParent !== null; });
    if (!focusable.length) return;
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (ev.shiftKey && document.activeElement === first) {
        ev.preventDefault();
        last.focus();
    } else if (!ev.shiftKey && document.activeElement === last) {
        ev.preventDefault();
        first.focus();
    }
}
