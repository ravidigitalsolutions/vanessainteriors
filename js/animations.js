/* =========================================================
   VANESSA INTERIORS — ANIMATIONS
   Scroll reveals (IntersectionObserver), staggered cards,
   number count-ups, smooth FAQ accordion and lightbox fade.
   Loaded in <head> so html.anim is set before first paint.
   Purely visual: no calculator, WhatsApp, popup or form logic
   lives here, and nothing here changes content or links.
   ========================================================= */
(function () {
    "use strict";

    var root = document.documentElement;
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var supported = "IntersectionObserver" in window && "requestAnimationFrame" in window;
    if (reduceMotion || !supported) return; // site stays fully static and visible
    root.classList.add("anim");

    /* ---------------------------------------------------------
       What gets animated — mapped onto the site's existing classes
       --------------------------------------------------------- */

    // groups whose direct children enter one after another
    var STAGGER_GROUPS = [
        ".grid", ".why-grid", ".value-list", ".process", ".mv-grid", ".chain",
        ".estimator-wrap", ".contact-list", ".footer-top", ".gallery-grid",
        ".project-grid.has-projects", ".pill-list", ".link-list"
    ];
    // single containers
    var SINGLES = [
        [".section-head", "reveal"],
        [".cta-band", "reveal-scale"],
        [".panel", "reveal"],
        [".coming-soon", "reveal"],
        [".review-empty", "reveal"],
        [".map-embed", "reveal-scale"],
        [".prose", "reveal"],
        [".faq", "reveal"],
        [".gallery-filters", "reveal-fade"],
        [".footer-bottom", "reveal-fade"],
        [".divider-rule", "reveal-fade"]
    ];
    var REVEAL_CLASSES = ["reveal", "reveal-left", "reveal-right", "reveal-scale", "reveal-fade", "stagger-item", "img-reveal"];
    var HERO = ".hero, .page-hero";

    var observer = null;

    // el.style can be shadowed (e.g. a <form> with a field named "style"),
    // so read the real CSSStyleDeclaration from the prototype
    var styleGetter = Object.getOwnPropertyDescriptor(HTMLElement.prototype, "style").get;
    function setVar(el, name, value) { styleGetter.call(el).setProperty(name, value); }
    function removeVar(el, name) { styleGetter.call(el).removeProperty(name); }

    // skip anything in a hero (animated on load) or inside an already-animated container
    function canTag(el) {
        if (el.closest(HERO)) return false;
        var parent = el.parentElement;
        while (parent && parent !== document.body) {
            if (parent.hasAttribute("data-anim")) return false;
            parent = parent.parentElement;
        }
        return true;
    }

    function tag(el, cls) {
        if (el.hasAttribute("data-anim") || !canTag(el)) return;
        REVEAL_CLASSES.forEach(function (c) { el.classList.remove(c); });
        el.classList.add(cls);
        el.setAttribute("data-anim", cls);
        if (observer) observer.observe(el);
    }

    function tagAll(scope) {
        scope = scope || document;

        // 1. two-column splits: left slides from the left, right from the right
        scope.querySelectorAll(".split, .contact-grid").forEach(function (split) {
            var kids = split.children;
            if (kids.length === 2 && canTag(split)) {
                tag(kids[0], "reveal-left");
                tag(kids[1], "reveal-right");
            }
        });

        // 2. repeated cards / items → stagger
        scope.querySelectorAll(STAGGER_GROUPS.join(",")).forEach(function (group) {
            if (!canTag(group)) return;
            Array.prototype.forEach.call(group.children, function (child) { tag(child, "stagger-item"); });
        });

        // 3. single containers
        SINGLES.forEach(function (pair) {
            scope.querySelectorAll(pair[0]).forEach(function (el) { tag(el, pair[1]); });
        });

        // 4. anything the HTML already marked with .reveal
        scope.querySelectorAll(".reveal:not([data-anim])").forEach(function (el) {
            if (el.closest(HERO)) { el.classList.remove("reveal"); return; }
            tag(el, "reveal");
        });
    }

    /* ---------------------------------------------------------
       IntersectionObserver — items revealed in the same frame
       share a batch and get a small stagger (--i), so nothing
       waits long even in long grids.
       --------------------------------------------------------- */
    function onIntersect(entries) {
        var batch = entries
            .filter(function (e) { return e.isIntersecting; })
            .map(function (e) { return e.target; })
            .sort(function (a, b) {
                return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
            });
        batch.forEach(function (el, index) {
            observer.unobserve(el);
            var i = el.classList.contains("stagger-item") ? Math.min(index, 6) : Math.min(index, 2);
            setVar(el, "--i", i);
            el.classList.add("is-visible");
            scheduleCleanup(el, i);
        });
    }

    // once revealed, hand the element back to its normal styles so
    // existing hover transforms/transitions work exactly as before
    function scheduleCleanup(el, i) {
        var step = window.innerWidth <= 720 ? 60 : 90;
        var duration = el.classList.contains("img-reveal") ? 1450 : (window.innerWidth <= 720 ? 650 : 900);
        setTimeout(function () {
            REVEAL_CLASSES.concat(["is-visible"]).forEach(function (c) { el.classList.remove(c); });
            removeVar(el, "--i");
            if (!el.getAttribute("style")) el.removeAttribute("style");
        }, duration + i * step + 60);
    }

    function initObserver() {
        observer = new IntersectionObserver(onIntersect, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
        document.querySelectorAll("[data-anim]").forEach(function (el) { observer.observe(el); });
    }

    // content injected later by other scripts (gallery grid, portfolio projects)
    function watchDynamic() {
        var grid = document.getElementById("galleryGrid");
        if (grid) {
            var first = true;
            new MutationObserver(function () {
                if (first) { first = false; tagAll(grid.parentElement); return; }
                // filter change: quick cascade instead of scroll reveal
                Array.prototype.forEach.call(grid.children, function (item, i) {
                    setVar(item, "--i", Math.min(i, 8));
                });
                grid.classList.remove("is-filtering");
                void grid.offsetWidth;
                grid.classList.add("is-filtering");
            }).observe(grid, { childList: true });
        }
        document.querySelectorAll("[data-portfolio-list]").forEach(function (list) {
            new MutationObserver(function () {
                if (list.classList.contains("has-projects")) {
                    Array.prototype.forEach.call(list.children, function (c) { tag(c, "stagger-item"); });
                }
            }).observe(list, { attributes: true, attributeFilter: ["class"] });
        });
    }

    /* ---------------------------------------------------------
       Number count-up (display only)
       --------------------------------------------------------- */
    function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }

    function countUp(el, target, format, duration, onDone) {
        var start = null;
        function frame(ts) {
            if (start === null) start = ts;
            var t = Math.min((ts - start) / duration, 1);
            el.textContent = format(target * easeOutCubic(t), t === 1);
            if (t < 1) requestAnimationFrame(frame);
            else if (onDone) onDone();
        }
        requestAnimationFrame(frame);
    }

    // hero stats: 14 / 100+ / 50+ / ₹5L
    function initStatCounters() {
        document.querySelectorAll(".hero .stat strong").forEach(function (el, i) {
            var original = el.textContent;
            var m = original.match(/^(\D*)(\d+)(\D*)$/);
            if (!m) return;
            var target = parseInt(m[2], 10);
            el.textContent = m[1] + "0" + m[3];
            setTimeout(function () {
                countUp(el, target, function (v, done) {
                    return done ? original : m[1] + Math.round(v) + m[3];
                }, 1400);
            }, 750 + i * 90);
        });
    }

    // estimator result: ₹0 → ₹16,00,000 (reads the text calculator.js wrote)
    function initEstimateCounter() {
        var total = document.querySelector('#estimateResult [data-slot="total"]');
        if (!total || typeof formatINR !== "function") return;
        var box = document.getElementById("estimateResult");
        var lastWritten = null;   // text this counter wrote itself
        var run = 0;              // a new calculation cancels the running count

        new MutationObserver(function () {
            var text = total.textContent;
            if (text === lastWritten) return;          // our own frame
            var finalText = text;                       // written by calculator.js
            var value = parseInt(finalText.replace(/[^\d]/g, ""), 10);
            if (!value) return;
            var id = ++run;
            var start = null;
            box.setAttribute("aria-busy", "true");
            function frame(ts) {
                if (id !== run) return;
                if (start === null) start = ts;
                var t = Math.min((ts - start) / 750, 1);
                lastWritten = t === 1 ? finalText : formatINR(value * easeOutCubic(t));
                total.textContent = lastWritten;
                if (t < 1) requestAnimationFrame(frame);
                else box.removeAttribute("aria-busy");
            }
            lastWritten = formatINR(0);
            total.textContent = lastWritten;
            requestAnimationFrame(frame);
        }).observe(total, { childList: true, characterData: true, subtree: true });
    }

    /* ---------------------------------------------------------
       FAQ — smooth open/close for the native <details> accordion
       --------------------------------------------------------- */
    function initFaq() {
        document.querySelectorAll(".faq details").forEach(function (details) {
            var summary = details.querySelector("summary");
            var answer = details.querySelector(".faq__answer");
            if (!summary || !answer || !answer.animate) return;
            var running = null;

            summary.addEventListener("click", function (ev) {
                ev.preventDefault();
                if (running) running.cancel();
                var opening = !details.open || details.classList.contains("is-closing");
                var startHeight = details.open ? answer.offsetHeight : 0;
                details.classList.remove("is-closing");

                if (opening) {
                    details.open = true;
                    var endHeight = answer.scrollHeight;
                    running = answer.animate(
                        [{ height: startHeight + "px", opacity: startHeight ? 1 : 0 }, { height: endHeight + "px", opacity: 1 }],
                        { duration: 380, easing: "cubic-bezier(.16, 1, .3, 1)" }
                    );
                } else {
                    details.classList.add("is-closing");
                    running = answer.animate(
                        [{ height: startHeight + "px", opacity: 1 }, { height: "0px", opacity: 0 }],
                        { duration: 280, easing: "cubic-bezier(.65, 0, .35, 1)" }
                    );
                }
                answer.style.overflow = "hidden";
                running.onfinish = function () {
                    if (!opening) {
                        details.open = false;
                        details.classList.remove("is-closing");
                    }
                    answer.style.overflow = "";
                    if (!answer.getAttribute("style")) answer.removeAttribute("style");
                    running = null;
                };
            });
        });
    }

    /* ---------------------------------------------------------
       Lightbox — fade out before gallery.js hides it
       (gallery.js keeps doing the actual closing)
       --------------------------------------------------------- */
    function initLightboxClose() {
        var passThrough = false;
        function animateThenClose(box) {
            box.classList.add("is-closing");
            setTimeout(function () {
                box.classList.remove("is-closing");
                passThrough = true;
                box.querySelector(".lightbox__close").click();
                passThrough = false;
            }, 200);
        }
        document.addEventListener("click", function (ev) {
            var box = document.getElementById("lightbox");
            if (!box || box.hidden || passThrough || box.classList.contains("is-closing")) return;
            if (ev.target === box || ev.target.closest(".lightbox__close")) {
                ev.stopPropagation();
                ev.preventDefault();
                animateThenClose(box);
            }
        }, true);
        window.addEventListener("keydown", function (ev) {
            var box = document.getElementById("lightbox");
            if (ev.key !== "Escape" || !box || box.hidden || box.classList.contains("is-closing")) return;
            ev.stopImmediatePropagation();
            animateThenClose(box);
        }, true);
    }

    /* --------------------------------------------------------- */
    document.addEventListener("DOMContentLoaded", function () {
        initObserver();
        tagAll(document);
        watchDynamic();
        initStatCounters();
        initEstimateCounter();
        initFaq();
        initLightboxClose();
    });
})();




document.addEventListener("DOMContentLoaded", () => {

    const revealElements =
        document.querySelectorAll(".reveal");

    const observer =
        new IntersectionObserver(
            (entries, observer) => {

                entries.forEach((entry) => {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("active");

                        observer.unobserve(
                            entry.target
                        );

                    }

                });

            },
            {
                threshold: 0.15
            }
        );

    revealElements.forEach((element) => {
        observer.observe(element);
    });

});