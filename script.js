(function () {
  var WHATSAPP_NUMBER = "5562996061223";

  document.querySelectorAll("[data-wa]").forEach(function (el) {
    var message = el.getAttribute("data-wa");
    el.setAttribute(
      "href",
      "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(message)
    );
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener");
  });

  // Scroll reveal: fades sections in as they enter view (hierarchy/pacing, not decoration).
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );
    document.querySelectorAll(".reveal").forEach(function (el) {
      observer.observe(el);
    });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) {
      el.classList.add("is-visible");
    });
  }
})();
