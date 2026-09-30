/* =========================================
   VIZAG SOLUTIONS SECTION
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    /* Initialize Lucide Icons */
    if (window.lucide) {
        window.lucide.createIcons();
    }


    /* Scroll Reveal Animation */
    const revealElements = document.querySelectorAll(
        ".vizag-solutions-section .reveal"
    );

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            function (entries, observer) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("active");

                        observer.unobserve(entry.target);

                    }

                });

            },
            {
                threshold: 0.12
            }
        );

        revealElements.forEach(function (element, index) {

            element.style.transitionDelay = (index * 70) + "ms";

            observer.observe(element);

        });

    } else {

        revealElements.forEach(function (element) {
            element.classList.add("active");
        });

    }

});