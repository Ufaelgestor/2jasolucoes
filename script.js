// Links work without JavaScript. Preserve the destination for each contact.
(function () {
  document.querySelectorAll('[data-wa]').forEach(function (link) {
    var number = link.getAttribute('data-wa-number') || '5562996061223';
    link.href = 'https://wa.me/' + number + '?text=' + encodeURIComponent(link.getAttribute('data-wa'));
  });

  // Product gallery: thumbnails swap the main photo.
  var foto = document.getElementById('produto-foto');
  var thumbs = document.querySelectorAll('[data-foto]');
  var nota = document.getElementById('foto-nota');
  thumbs.forEach(function (thumb) {
    thumb.addEventListener('click', function (event) {
      event.preventDefault();
      foto.src = thumb.href;
      foto.classList.toggle('is-contain', thumb.hasAttribute('data-contain'));
      if (nota) nota.hidden = !thumb.hasAttribute('data-ia');
      thumbs.forEach(function (other) { other.classList.toggle('is-active', other === thumb); });
    });
  });
})();
