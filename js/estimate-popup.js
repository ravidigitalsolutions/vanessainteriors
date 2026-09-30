document.addEventListener("DOMContentLoaded", function () {

    const modal = document.getElementById("estimateModal");
    const openBtn = document.getElementById("openEstimatePopup");
    const closeBtn = document.getElementById("closeEstimatePopup");
    const overlay = document.getElementById("estimateOverlay");
    const form = document.getElementById("estimateForm");

    // Open Popup
    openBtn.addEventListener("click", function () {
        modal.classList.add("is-open");
        document.body.style.overflow = "hidden";
    });

    // Close Popup
    function closePopup() {
        modal.classList.remove("is-open");
        document.body.style.overflow = "";
    }

    closeBtn.addEventListener("click", closePopup);
    overlay.addEventListener("click", closePopup);

    // Close on Escape
    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closePopup();
        }
    });

    // Form Submit → WhatsApp
    form.addEventListener("submit", function (event) {

        event.preventDefault();

        const name = document.getElementById("estimateName").value.trim();
        const phone = document.getElementById("estimatePhone").value.trim();
        const service = document.getElementById("estimateService").value;
        const area = document.getElementById("estimateArea").value.trim();

        if (!/^[0-9]{10}$/.test(phone)) {
            alert("Please enter a valid 10-digit phone number.");
            return;
        }

        const businessWhatsApp = "919291199999";

        const message =
            "Hello Vanessa Interiors!%0A%0A" +
            "I would like to get a free interior estimate.%0A%0A" +
            "Name: " + encodeURIComponent(name) + "%0A" +
            "Phone: " + encodeURIComponent(phone) + "%0A" +
            "Service: " + encodeURIComponent(service) + "%0A" +
            (area ? "Area: " + encodeURIComponent(area) + " SFT%0A" : "") +
            "%0APlease contact me with the estimate and details.";

        const whatsappURL =
            "https://wa.me/" + businessWhatsApp + "?text=" + message;

        window.open(whatsappURL, "_blank", "noopener,noreferrer");

    });

});