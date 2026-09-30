/* =========================================================
   VANESSA INTERIORS — CENTRAL CONFIGURATION
   Every calculator, popup, form and WhatsApp function reads
   from this file. Change values here only.
   ========================================================= */

const SITE_CONFIG = {
    businessName: "Vanessa Interiors",
    whatsappNumber: "919291199999",          // used for https://wa.me/919291199999
    phone: "+91 9291199999",                 // display format
    phoneLink: "+919291199999",              // tel: link format
    email: "vanessainteriors@mail.com",
    website: "https://www.vanessainteriors.in",
    instagram: "https://www.instagram.com/vanessainteriorsindia/",
    address: "Aruna Inn, 49-24-16, Sankara Matam Road, Madhuranagar, Akkayyapalem, Visakhapatnam, Andhra Pradesh – 530016",

    /* Optional: paste a form-handling endpoint (Formspree, Google Apps Script,
       your own server…) to receive enquiries as JSON. When left empty, form
       submissions open WhatsApp with the enquiry details pre-filled. */
    formEndpoint: ""
};

/* ---------- Cost estimator ---------- */

/* Base rate in ₹ per sq.ft. — the ONLY place the base rate is defined. */
const COST_PER_SQFT = 1600;

/* Per-category rates. All use the base rate for now.
   To price a category differently later, replace COST_PER_SQFT
   with a number, e.g.  kitchen: 1800,  bedroom: 1700, */
const INTERIOR_PRICES = {
    /*completeHome: COST_PER_SQFT,
    kitchen: COST_PER_SQFT,
    wardrobes: COST_PER_SQFT,
    bedroom: COST_PER_SQFT,
    livingArea: COST_PER_SQFT
};*/
    completeHome: 1600,
    kitchen: 900,
    wardrobes: 1200,
    bedroom: 1200,
    livingArea: 850
};

/* Display names for each estimator category (keys match INTERIOR_PRICES). */
const INTERIOR_TYPES = {
    completeHome: "Complete Home Interior",
    kitchen: "Kitchen",
    wardrobes: "Wardrobes",
    bedroom: "Bedroom",
    livingArea: "Living Area"
};

/* Accepted area range for the estimator (sq.ft.). */
const AREA_LIMITS = { min: 1, max: 100000 };

const ESTIMATE_DISCLAIMER =
    "Estimated cost is for initial planning purposes only. Final project pricing may vary depending on design requirements, materials, specifications, site conditions and project scope.";

/* Services offered — used by the popup and contact form service lists. */
const SERVICES = [
    "Home Interiors",
    "Modular Kitchen",
    "Bedroom Design",
    "Living Room Design",
    "Wardrobes",
    "False Ceiling",
    "Office Interiors",
    "Commercial Interiors",
    "Villa Interiors",
    "Renovation Services",
    "Turnkey Interiors"
];

/* ---------- Shared helpers ---------- */

/* Formats a number in Indian currency style: 2400000 -> ₹24,00,000 */
function formatINR(amount) {
    return "₹" + Math.round(amount).toLocaleString("en-IN");
}

/* Formats an area value: 1250.5 -> 1,250.5 */
function formatArea(area) {
    return Number(area.toFixed(2)).toLocaleString("en-IN", { maximumFractionDigits: 2 });
}
