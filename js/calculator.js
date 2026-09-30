/* =========================================================
   INTERIOR COST ESTIMATOR
   Total = Entered area × INTERIOR_PRICES[selected type]
   Rates live in js/config.js (COST_PER_SQFT / INTERIOR_PRICES).
   ========================================================= */

window.lastEstimate = null;

function getCheckedValue(form, name) {
    const el = form.querySelector('input[name="' + name + '"]:checked');
    return el ? el.value : "";
}

function setEstimatorError(form, name, message) {
    const holder = form.querySelector('[data-est-error="' + name + '"]');
    if (holder) holder.textContent = message || "";
    const group = form.querySelector('[data-est-group="' + name + '"]');
    if (group) group.classList.toggle("has-error", !!message);
}

function calculateEstimate() {
    const form = document.getElementById("estimatorForm");
    if (!form) return null;

    const typeKey = getCheckedValue(form, "interiorType");
    const areaInput = form.querySelector('[name="area"]');
    const areaError = validateAreaValue(areaInput.value, true); // forms.js
    const property = getCheckedValue(form, "propertyType");
    const style = getCheckedValue(form, "style");
    const timeline = getCheckedValue(form, "timeline");

    const checks = [
        ["interiorType", typeKey ? "" : "Please select what you would like to estimate."],
        ["area", areaError],
        ["propertyType", property ? "" : "Please select your property type."],
        ["style", style ? "" : "Please select a preferred style."],
        ["timeline", timeline ? "" : "Please select your project timeline."]
    ];
    let firstError = null;
    checks.forEach(function (c) {
        setEstimatorError(form, c[0], c[1]);
        if (c[1] && !firstError) firstError = c[0];
    });
    areaInput.classList.toggle("is-invalid", !!areaError);
    areaInput.setAttribute("aria-invalid", areaError ? "true" : "false");

    if (firstError) {
        const target = form.querySelector('[data-est-group="' + firstError + '"]');
        if (target) target.scrollIntoView({ behavior: "smooth", block: "center" });
        if (firstError === "area") areaInput.focus();
        return null;
    }

    const area = parseFloat(areaInput.value.replace(/,/g, ""));
    const rate = INTERIOR_PRICES[typeKey];
    const estimate = {
        typeKey: typeKey,
        typeLabel: INTERIOR_TYPES[typeKey],
        area: area,
        rate: rate,
        total: area * rate,
        property: property,
        style: style,
        timeline: timeline
    };
    window.lastEstimate = estimate;
    renderEstimate(estimate);
    return estimate;
}

function renderEstimate(e) {
    const box = document.getElementById("estimateResult");
    if (!box) return;
    function slot(name, value) {
        const el = box.querySelector('[data-slot="' + name + '"]');
        if (el) el.textContent = value;
    }
    slot("total", formatINR(e.total));
    slot("calc", formatArea(e.area) + " sq.ft. × " + formatINR(e.rate));
    slot("type", e.typeLabel);
    slot("area", formatArea(e.area) + " sq.ft.");
    slot("property", e.property);
    slot("style", e.style);
    slot("timeline", e.timeline);

    const leadBtn = box.querySelector("[data-estimate-lead]");
    if (leadBtn) leadBtn.setAttribute("data-lead", e.typeLabel);

    box.hidden = false;
    box.classList.remove("is-shown");
    void box.offsetWidth; // restart the reveal animation
    box.classList.add("is-shown");
    box.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

/* Shows the configured rate next to each category card. */
function renderEstimatorRates(form) {
    form.querySelectorAll("[data-rate-for]").forEach(function (el) {
        const rate = INTERIOR_PRICES[el.getAttribute("data-rate-for")];
        if (rate) el.textContent = formatINR(rate) + "/sq.ft.";
    });
}

function initEstimator() {
    const form = document.getElementById("estimatorForm");
    if (!form) return;
    renderEstimatorRates(form);

    // pre-select a category from ?type=kitchen (links from service pages)
    const params = new URLSearchParams(window.location.search);
    const preset = params.get("type");
    if (preset && INTERIOR_PRICES[preset]) {
        const radio = form.querySelector('input[name="interiorType"][value="' + preset + '"]');
        if (radio) radio.checked = true;
    }

    form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        calculateEstimate();
    });

    // clear a group's error as soon as the visitor fixes it
    form.addEventListener("change", function (ev) {
        if (ev.target.name && ev.target.type === "radio") setEstimatorError(form, ev.target.name, "");
    });
    const areaInput = form.querySelector('[name="area"]');
    areaInput.addEventListener("input", function () {
        const msg = areaInput.value.trim() ? validateAreaValue(areaInput.value, true) : "";
        setEstimatorError(form, "area", msg);
        areaInput.classList.toggle("is-invalid", !!msg);
    });
}

document.addEventListener("DOMContentLoaded", initEstimator);
