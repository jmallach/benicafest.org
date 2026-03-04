// Benicafest — main.js

// Show sticky nav after scrolling past hero
(function () {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  function onScroll() {
    const threshold = window.innerHeight * 0.5;
    navbar.classList.toggle('visible', window.scrollY > threshold);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // run once on load
})();
