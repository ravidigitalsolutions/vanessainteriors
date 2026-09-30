/* =========================================================
   FORMS — validation + delivery for the popup and contact form.
   Delivery: POSTs JSON to SITE_CONFIG.formEndpoint when set;
   otherwise opens WhatsApp with the enquiry pre-filled.
   ========================================================= */

/* ---------- validation helpers ---------- */

function cleanPhone(value) {
    let digits = String(value || "").replace(/\D/g, "");
    if (digits.length === 12 && digits.indexOf("91") === 0) digits = digits.slice(2);
    if (digits.length === 11 && digits.charAt(0) === "0") digits = digits.slice(1);
    return digits;
}

function isValidPhone(value) {
    return /^[6-9]\d{9}$/.test(cleanPhone(value));
}

/* Returns an error message, or "" when the area is valid.
   required=false lets an empty value pass (popup & contact form). */
function validateAreaValue(raw, required) {
    const value = String(raw || "").replace(/,/g, "").trim();
    if (!value) return required ? "Please enter your area in sq.ft." : "";
    if (/^-/.test(value)) return "Area cannot be negative.";
    if (!/^\d*\.?\d+$/.test(value)) return "Please enter numbers only (e.g. 1250 or 1250.5).";
    const num = parseFloat(value);
    if (num === 0) return "Area cannot be zero.";
    if (num < AREA_LIMITS.min) return "Please enter at least " + AREA_LIMITS.min + " sq.ft.";
    if (num > AREA_LIMITS.max) return "For areas above " + AREA_LIMITS.max.toLocaleString("en-IN") + " sq.ft., please contact us directly.";
    return "";
}

function setFieldError(form, name, message) {
    const input = form.querySelector('[name="' + name + '"]');
    const holder = form.querySelector('[data-error-for="' + name + '"]');
    if (input) {
        input.classList.toggle("is-invalid", !!message);
        input.setAttribute("aria-invalid", message ? "true" : "false");
    }
    if (holder) holder.textContent = message || "";
}

function clearFormErrors(form) {
    form.querySelectorAll(".is-invalid").forEach(function (el) {
        el.classList.remove("is-invalid");
        el.removeAttribute("aria-invalid");
    });
    form.querySelectorAll(".field__error").forEach(function (el) { el.textContent = ""; });
}

/* Validates the shared lead fields. Returns true when valid. */
function validateLeadFields(form) {
    clearFormErrors(form);
    const data = new FormData(form);
    let firstInvalid = null;
    function fail(name, msg) {
        setFieldError(form, name, msg);
        if (!firstInvalid) firstInvalid = form.querySelector('[name="' + name + '"]');
    }

    const name = String(data.get("name") || "").trim();
    if (name.length < 2) fail("name", "Please enter your name.");

    const phone = String(data.get("phone") || "").trim();
    if (!phone) fail("phone", "Please enter your phone number.");
    else if (!isValidPhone(phone)) fail("phone", "Please enter a valid 10-digit mobile number.");

    if (data.has("whatsapp")) {
        const wa = String(data.get("whatsapp") || "").trim();
        if (wa && !isValidPhone(wa)) fail("whatsapp", "Please enter a valid 10-digit number.");
    }

    if (data.has("area")) {
        const areaError = validateAreaValue(data.get("area"), false);
        if (areaError) fail("area", areaError);
    }

    if (data.has("email")) {
        const email = String(data.get("email") || "").trim();
        if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) fail("email", "Please enter a valid email address.");
    }

    if (firstInvalid) firstInvalid.focus();
    return !firstInvalid;
}

/* ---------- delivery ---------- */

const LEAD_LABELS = {
    service: "Interested Service",
    name: "Name",
    phone: "Phone",
    whatsapp: "WhatsApp Number",
    email: "Email",
    propertyType: "Property Type",
    area: "Area",
    location: "Project Location",
    budget: "Estimated Budget",
    message: "Message"
};

function collectLead(form, source) {
    const data = { source: source, page: document.title };
    new FormData(form).forEach(function (value, key) {
        const v = String(value).trim();
        if (v) data[key] = v;
    });
    if (window.lastEstimate) {
        data.estimate = window.lastEstimate.typeLabel + " · " + formatArea(window.lastEstimate.area) +
            " sq.ft. · " + formatINR(window.lastEstimate.total);
    }
    return data;
}

function leadToMessage(data) {
    const lines = ["Hello " + SITE_CONFIG.businessName + ",", "", "I would like to enquire about an interior project.", ""];
    Object.keys(LEAD_LABELS).forEach(function (key) {
        if (data[key]) lines.push(LEAD_LABELS[key] + ": " + data[key] + (key === "area" ? " sq.ft." : ""));
    });
    if (data.estimate) lines.push("Estimator result: " + data.estimate);
    lines.push("", "Please contact me.", "", "Thank you.");
    return lines.join("\n");
}

/* Sends the lead. Returns a Promise that resolves to "endpoint" or "whatsapp". */
function deliverLead(data) {
    if (SITE_CONFIG.formEndpoint) {
        return fetch(SITE_CONFIG.formEndpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json", "Accept": "application/json" },
            body: JSON.stringify(data)
        }).then(function (res) {
            if (!res.ok) throw new Error("Request failed");
            return "endpoint";
        });
    }
    openWhatsAppMessage(leadToMessage(data)); // must run synchronously inside the click
    return Promise.resolve("whatsapp");
}

function successText(channel) {
    return channel === "whatsapp"
        ? "WhatsApp has opened with your enquiry details — just press send and our team will get back to you."
        : "Your enquiry has been received. Our team will contact you shortly.";
}

/* ---------- popup form ---------- */

function handleLeadSubmit(ev) {
    ev.preventDefault();
    const form = ev.currentTarget;
    if (!validateLeadFields(form)) return;
    const button = form.querySelector('[type="submit"]');
    button.disabled = true;

    deliverLead(collectLead(form, "Popup — " + document.getElementById("leadTitle").textContent))
        .then(function (channel) {
            document.getElementById("leadSuccessText").textContent = successText(channel);
            form.hidden = true;
            form.reset();
            document.getElementById("leadSuccess").hidden = false;
        })
        .catch(function () {
            setFieldError(form, "phone", "Sorry, we could not send your enquiry. Please try WhatsApp or call us.");
        })
        .then(function () { button.disabled = false; });
}

/* ---------- contact page form ---------- */

function initContactForm() {
    const form = document.getElementById("contactForm");
    if (!form) return;

    const select = form.querySelector('[name="service"]');
    if (select && select.options.length <= 1) {
        SERVICES.forEach(function (name) {
            const opt = document.createElement("option");
            opt.value = name;
            opt.textContent = name;
            select.appendChild(opt);
        });
    }

    form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        if (!validateLeadFields(form)) return;
        const status = document.getElementById("contactStatus");
        const button = form.querySelector('[type="submit"]');
        button.disabled = true;
        deliverLead(collectLead(form, "Contact page"))
            .then(function (channel) {
                status.textContent = successText(channel);
                status.className = "form-status is-success";
                form.reset();
            })
            .catch(function () {
                status.textContent = "Sorry, we could not send your enquiry. Please call or WhatsApp us on " + SITE_CONFIG.phone + ".";
                status.className = "form-status is-error";
            })
            .then(function () { button.disabled = false; });
    });
}

document.addEventListener("DOMContentLoaded", initContactForm);
