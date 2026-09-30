/* =========================================================
   PORTFOLIO — renders verified projects on the portfolio pages.
   ADD GENUINE PROJECTS to PORTFOLIO_PROJECTS. Only publish details
   (location, size, services) that you have verified.

   Example:
   {
       category: "residential",          // residential | commercial | villas | apartments
       name: "Actual Project Name",
       location: "Verified Location",
       propertyType: "Apartment",
       services: "Modular Kitchen, Wardrobes, False Ceiling",
       style: "Modern",
       description: "Original project description.",
       images: ["images/portfolio/project-name-living-room.webp"]
   }
   ========================================================= */

const PORTFOLIO_PROJECTS = [
    // Add verified projects here.
];

(function () {
    function root() {
        return document.body.getAttribute("data-root") || "";
    }

    function projectCard(p) {
        const img = p.images && p.images.length
            ? '<img src="' + root() + p.images[0] + '" alt="' + p.name + ' — interior design by Vanessa Interiors" loading="lazy">'
            : "";
        const rows = [
            ["Location", p.location],
            ["Property Type", p.propertyType],
            ["Business Type", p.businessType],
            ["Services", p.services],
            ["Design Style", p.style]
        ].filter(function (r) { return r[1]; })
         .map(function (r) { return "<div><dt>" + r[0] + "</dt><dd>" + r[1] + "</dd></div>"; }).join("");
        return '<article class="project-card">' +
            '<div class="project-card__media">' + img + "</div>" +
            '<div class="project-card__body"><h3>' + p.name + "</h3>" +
            '<dl class="project-card__meta">' + rows + "</dl>" +
            (p.description ? "<p>" + p.description + "</p>" : "") +
            "</div></article>";
    }

    function init() {
        document.querySelectorAll("[data-portfolio-list]").forEach(function (list) {
            const cat = list.getAttribute("data-portfolio-list");
            const projects = PORTFOLIO_PROJECTS.filter(function (p) { return cat === "all" || p.category === cat; });
            if (!projects.length) return; // keep the page's "coming soon" note
            list.innerHTML = projects.map(projectCard).join("");
            list.classList.add("has-projects");
        });
    }

    document.addEventListener("DOMContentLoaded", init);
})();
