/* =========================================================
   WHATSAPP — one reusable set of functions for every CTA.
   Buttons use:  data-whatsapp="Modular Kitchen"
   (main.js wires them to openWhatsApp automatically)
   ========================================================= */

function buildWhatsAppUrl(message) {
    return "https://wa.me/" + SITE_CONFIG.whatsappNumber + "?text=" + encodeURIComponent(message);
}

function openWhatsAppMessage(message) {
    const url = buildWhatsAppUrl(message);
    const win = window.open(url, "_blank");
    if (win) {
        win.opener = null;
    } else {
        window.location.href = url; // popup blocked — open in same tab
    }
}

/* Service-specific message. Called with no name for a general enquiry. */
function openWhatsApp(serviceName) {
    const name = (serviceName || "").trim();
    const message = name
        ? "Hello " + SITE_CONFIG.businessName + ",\n\n" +
          "I am interested in your " + name + " service.\n\n" +
          "I would like to discuss my requirements and get an estimated cost.\n\n" +
          "Please contact me.\n\n" +
          "Thank you."
        : "Hello " + SITE_CONFIG.businessName + ",\n\n" +
          "I would like to discuss my interior design requirements.\n\n" +
          "Please contact me.\n\n" +
          "Thank you.";
    openWhatsAppMessage(message);
}

/* Sends the latest cost-estimator result (set by calculator.js). */
function openEstimateWhatsApp() {
    const e = window.lastEstimate;
    if (!e) {
        openWhatsApp("Interior Cost Estimate");
        return;
    }
    const message =
        "Hello " + SITE_CONFIG.businessName + ",\n\n" +
        "I used your Interior Cost Estimator.\n\n" +
        "Interior Type: " + e.typeLabel + "\n" +
        "Area: " + formatArea(e.area) + " sq.ft.\n" +
        "Property Type: " + e.property + "\n" +
        "Preferred Style: " + e.style + "\n" +
        "Timeline: " + e.timeline + "\n" +
        "Estimated Cost: " + formatINR(e.total) + "\n\n" +
        "I would like to discuss my project in detail.\n\n" +
        "Thank you.";
    openWhatsAppMessage(message);
}
