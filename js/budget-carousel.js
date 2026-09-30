/* =========================================
   BUDGET CAROUSEL + ENQUIRY POPUP
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    const carousel = document.getElementById("budgetCarousel");
    const prevBtn = document.querySelector(".budget-prev");
    const nextBtn = document.querySelector(".budget-next");

    const modal = document.getElementById("budgetModal");
    const closeBtn = document.getElementById("closeBudgetModal");
    const openQuoteBtn = document.getElementById("openBudgetForm");

    const packageName = document.getElementById("selectedPackage");
    const packagePrice = document.getElementById("selectedPrice");

    const form = document.getElementById("budgetEnquiryForm");

    let selectedPackage = "General Enquiry";
    let selectedPrice = "";

    /* =========================================
       CAROUSEL NAVIGATION
    ========================================= */

    function getScrollAmount() {
        const card = carousel.querySelector(".budget-card");

        if (!card) return 300;

        const gap = parseFloat(
            getComputedStyle(carousel.querySelector(".budget-track")).gap
        ) || 0;

        return card.getBoundingClientRect().width + gap;
    }

    nextBtn.addEventListener("click", function () {
        carousel.scrollBy({
            left: getScrollAmount(),
            behavior: "smooth"
        });
    });

    prevBtn.addEventListener("click", function () {
        carousel.scrollBy({
            left: -getScrollAmount(),
            behavior: "smooth"
        });
    });


    /* =========================================
       OPEN POPUP
    ========================================= */

    function openModal(packageNameText, priceText) {

        selectedPackage = packageNameText || "General Enquiry";
        selectedPrice = priceText || "";

        packageName.textContent = selectedPackage;

        packagePrice.textContent = selectedPrice
            ? "Starting at ₹" + selectedPrice + "L*"
            : "Our team will discuss your requirements.";

        modal.classList.add("is-open");
        modal.setAttribute("aria-hidden", "false");

        document.body.style.overflow = "hidden";

        document.getElementById("budgetName").focus();
    }


    /* =========================================
       CLOSE POPUP
    ========================================= */

    function closeModal() {

        modal.classList.remove("is-open");
        modal.setAttribute("aria-hidden", "true");

        document.body.style.overflow = "";

    }


    /* =========================================
       CARD CLICK
    ========================================= */

    document.querySelectorAll(".budget-card").forEach(function (card) {

        card.addEventListener("click", function () {

            const packageText = card.dataset.package;
            const priceText = card.dataset.price;

            openModal(packageText, priceText);

        });

    });


    /* GET FREE QUOTE BUTTON */

    openQuoteBtn.addEventListener("click", function () {
        openModal("General Enquiry", "");
    });


    /* CLOSE BUTTON */

    closeBtn.addEventListener("click", closeModal);


    /* CLICK OUTSIDE POPUP */

    modal.querySelectorAll("[data-close-modal]").forEach(function (element) {
        element.addEventListener("click", closeModal);
    });


    /* ESCAPE KEY */

    document.addEventListener("keydown", function (event) {

        if (event.key === "Escape" && modal.classList.contains("is-open")) {
            closeModal();
        }

    });


    /* =========================================
       FORM SUBMIT → WHATSAPP
    ========================================= */

    form.addEventListener("submit", function (event) {

        event.preventDefault();

        const name = document.getElementById("budgetName").value.trim();
        const phone = document.getElementById("budgetPhone").value.trim();
        const whatsapp = document.getElementById("budgetWhatsApp").value.trim();

        if (!/^[0-9]{10}$/.test(phone)) {
            alert("Please enter a valid 10-digit phone number.");
            return;
        }

        if (!/^[0-9]{10}$/.test(whatsapp)) {
            alert("Please enter a valid 10-digit WhatsApp number.");
            return;
        }

        const businessWhatsApp = "919291199999";

        const message =
            "Hello Vanessa Interiors,%0A%0A" +
            "I am interested in an interior design package.%0A%0A" +
            "Name: " + encodeURIComponent(name) + "%0A" +
            "Phone: " + encodeURIComponent(phone) + "%0A" +
            "WhatsApp: " + encodeURIComponent(whatsapp) + "%0A" +
            "Selected Package: " + encodeURIComponent(selectedPackage) + "%0A" +
            (selectedPrice
                ? "Starting Price: ₹" + encodeURIComponent(selectedPrice) + "L*%0A"
                : "") +
            "%0APlease contact me with more details.";

        const whatsappURL =
            "https://wa.me/" + businessWhatsApp + "?text=" + message;

        window.open(whatsappURL, "_blank", "noopener,noreferrer");

    });

});