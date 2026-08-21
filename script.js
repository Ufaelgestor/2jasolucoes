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
})();
