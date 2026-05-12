/* Global performance and UX helpers */
(function () {
  "use strict";

  // Lazy-load CSS background images declared as data-bg.
  var bgNodes = document.querySelectorAll("[data-bg]");
  if ("IntersectionObserver" in window && bgNodes.length) {
    var io = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var node = entry.target;
        var bg = node.getAttribute("data-bg");
        if (bg) node.style.backgroundImage = "url('" + bg + "')";
        observer.unobserve(node);
      });
    });
    bgNodes.forEach(function (node) {
      io.observe(node);
    });
  }

  // Improve external link safety.
  document.querySelectorAll('a[target="_blank"]').forEach(function (link) {
    if (!link.rel || link.rel.indexOf("noopener") === -1) {
      link.rel = (link.rel ? link.rel + " " : "") + "noopener noreferrer";
    }
  });
})();
