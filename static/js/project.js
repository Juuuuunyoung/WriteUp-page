document.addEventListener('DOMContentLoaded', function () {
  var cards = document.querySelectorAll('.card');
  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      var url = card.getAttribute('data-url');
      window.location.href = url;
    });
  });
});