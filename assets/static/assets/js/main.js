  window.addEventListener('scroll', function () {
    const header = document.getElementById('navbar');
    if (window.scrollY > 20) {
      header.classList.remove('transparent');
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
      header.classList.add('transparent');
    }
  });

  // Set initial state
  window.addEventListener('DOMContentLoaded', function () {
    const header = document.getElementById('navbar');
    if (window.scrollY <= 20) {
      header.classList.add('transparent');
    }
  });

