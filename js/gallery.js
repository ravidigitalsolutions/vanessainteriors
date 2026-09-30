/* =========================================================
   GALLERY — filterable grid + lightbox.
   ADD YOUR PROJECT PHOTOS to GALLERY_ITEMS below, e.g.
   { src: "images/gallery/luxury-living-room-interiors-visakhapatnam.webp",
     category: "Living Room",
     alt: "Luxury living room interior design by Vanessa Interiors" }
   Items marked placeholder:true are design illustrations shown
   until real photographs are added — delete them when you do.
   ========================================================= */

const GALLERY_CATEGORIES = [
    "Living Room",
    "Bedroom",
    "Modular Kitchen",
    "Wardrobes",
    "False Ceiling",
    "Villa Interiors",
    "Office Interiors",
    "Commercial Interiors"
];

const GALLERY_ITEMS = [
    { src: "images/services/living-room.svg", category: "Living Room", alt: "Living room design illustration", placeholder: true },
    { src: "images/services/bedroom-design.svg", category: "Bedroom", alt: "Bedroom design illustration", placeholder: true },
    { src: "images/services/modular-kitchen.svg", category: "Modular Kitchen", alt: "Modular kitchen design illustration", placeholder: true },
    { src: "images/services/wardrobes.svg", category: "Wardrobes", alt: "Wardrobe design illustration", placeholder: true },
    { src: "images/services/false-ceiling.svg", category: "False Ceiling", alt: "False ceiling design illustration", placeholder: true },
    { src: "images/services/villa-interiors.svg", category: "Villa Interiors", alt: "Villa interiors illustration", placeholder: true },
    { src: "images/services/office-interiors.svg", category: "Office Interiors", alt: "Office interiors illustration", placeholder: true },
    { src: "images/services/commercial-interiors.svg", category: "Commercial Interiors", alt: "Commercial interiors illustration", placeholder: true }
];

(function () {
    let visible = [];
    let current = 0;

    function init() {
        const grid = document.getElementById("galleryGrid");
        const filters = document.getElementById("galleryFilters");
        if (!grid) return;

        const cats = ["All"].concat(GALLERY_CATEGORIES);
        filters.innerHTML = cats.map(function (c, i) {
            return '<button type="button" class="chip' + (i === 0 ? " is-active" : "") + '" data-filter="' + c + '" aria-pressed="' + (i === 0) + '">' + c + "</button>";
        }).join("");
        filters.addEventListener("click", function (ev) {
            const btn = ev.target.closest("[data-filter]");
            if (!btn) return;
            filters.querySelectorAll(".chip").forEach(function (b) {
                b.classList.toggle("is-active", b === btn);
                b.setAttribute("aria-pressed", String(b === btn));
            });
            render(btn.getAttribute("data-filter"));
        });
        render("All");
        buildLightbox();
    }

    function render(filter) {
        const grid = document.getElementById("galleryGrid");
        visible = GALLERY_ITEMS.filter(function (item) { return filter === "All" || item.category === filter; });
        if (!visible.length) {
            grid.innerHTML = '<p class="empty-note">Photographs for this category are being added. <a href="contact.html">Contact us</a> to see recent work.</p>';
            return;
        }
        grid.innerHTML = visible.map(function (item, i) {
            return '<figure class="gallery-item' + (item.placeholder ? " is-placeholder" : "") + '">' +
                '<button type="button" class="gallery-item__btn" data-index="' + i + '" aria-label="Open ' + item.alt + '">' +
                '<img src="' + item.src + '" alt="' + item.alt + '" loading="lazy" width="800" height="600">' +
                "</button>" +
                "<figcaption><span>" + item.category + "</span>" +
                (item.placeholder ? '<small>Project photographs coming soon</small>' : "") +
                "</figcaption></figure>";
        }).join("");
        grid.querySelectorAll(".gallery-item__btn").forEach(function (btn) {
            btn.addEventListener("click", function () { open(parseInt(btn.getAttribute("data-index"), 10)); });
        });
    }

    function buildLightbox() {
        const box = document.createElement("div");
        box.className = "lightbox";
        box.id = "lightbox";
        box.hidden = true;
        box.setAttribute("role", "dialog");
        box.setAttribute("aria-modal", "true");
        box.setAttribute("aria-label", "Image viewer");
        box.innerHTML =
            '<button type="button" class="lightbox__close" aria-label="Close">×</button>' +
            '<button type="button" class="lightbox__nav lightbox__prev" aria-label="Previous">‹</button>' +
            '<figure class="lightbox__figure"><img alt=""><figcaption></figcaption></figure>' +
            '<button type="button" class="lightbox__nav lightbox__next" aria-label="Next">›</button>';
        document.body.appendChild(box);
        box.querySelector(".lightbox__close").addEventListener("click", close);
        box.querySelector(".lightbox__prev").addEventListener("click", function () { show(current - 1); });
        box.querySelector(".lightbox__next").addEventListener("click", function () { show(current + 1); });
        box.addEventListener("click", function (ev) { if (ev.target === box) close(); });
        document.addEventListener("keydown", function (ev) {
            if (box.hidden) return;
            if (ev.key === "Escape") close();
            if (ev.key === "ArrowLeft") show(current - 1);
            if (ev.key === "ArrowRight") show(current + 1);
        });
    }

    function show(i) {
        current = (i + visible.length) % visible.length;
        const item = visible[current];
        const box = document.getElementById("lightbox");
        box.querySelector("img").src = item.src;
        box.querySelector("img").alt = item.alt;
        box.querySelector("figcaption").textContent = item.category + (item.placeholder ? " — design illustration" : "");
    }

    function open(i) {
        show(i);
        const box = document.getElementById("lightbox");
        box.hidden = false;
        document.body.classList.add("modal-open");
        box.querySelector(".lightbox__close").focus();
    }

    function close() {
        document.getElementById("lightbox").hidden = true;
        document.body.classList.remove("modal-open");
    }

    document.addEventListener("DOMContentLoaded", init);
})();
