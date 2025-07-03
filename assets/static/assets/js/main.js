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

// Technologies we use  
document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".tab-btn");
  const panels = document.querySelectorAll(".tab-panel");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      // Remove active class from all
      buttons.forEach(b => b.classList.remove("active"));
      panels.forEach(p => p.classList.remove("active"));

      // Add active to clicked
      btn.classList.add("active");
      const target = btn.getAttribute("data-tab");
      document.getElementById(target).classList.add("active");
    });
  });
});

// Testimonial
document.addEventListener("DOMContentLoaded", function () {
  const swiper = new Swiper('.testimonial-swiper', {
    loop: true,
    autoplay: {
      delay: 5000,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
});


// Portfolio
  document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll('.portfolio-card');

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        } else {
          entry.target.classList.remove('active');
        }
      });
    }, {
      threshold: 0.6 // means 60% of card is visible
    });

    cards.forEach(card => observer.observe(card));
  });