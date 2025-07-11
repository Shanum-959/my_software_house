// Navbar
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

// Chatbot
document.addEventListener('DOMContentLoaded', () => {
    const chatToggle = document.querySelector('#chat-toggle');
    const chatPopup  = document.querySelector('#chat-popup');
    const chatClose  = document.querySelector('.chat-close');
    const chatSend   = document.querySelector('#chat-send');
    const chatInput  = document.querySelector('#chat-input');
    const chatBody   = document.querySelector('#chat-body');

    /* --- utility: صحیح URL خودکار نکالیں --- */
    const getChatUrl = () => {
        const parts = window.location.pathname.split('/');
        const first = parts[1];            // '' | 'en' | 'ur' | ...
        const twoLetterLang = /^[a-z]{2}$/i;
        if (twoLetterLang.test(first)) {
            return `/${first}/chatbot/message/`;   // ‎/en/chat/message/‎
        }
        return `/chatbot/message/`;               // ‎/chat/message/‎
    };

    /* ------------- widget toggle ------------- */
    if (chatToggle && chatPopup) {
        chatToggle.addEventListener('click', () => {
            const opened = chatPopup.classList.toggle('active');
            chatPopup.setAttribute('aria-hidden', opened ? 'false' : 'true');
            if (opened) chatInput.focus();
        });

        chatClose.addEventListener('click', () => {
            chatPopup.classList.remove('active');
            chatPopup.setAttribute('aria-hidden', 'true');
            chatToggle.focus();
        });

        /* ------------- message send ------------- */
        const sendMessage = async () => {
            const message = chatInput.value.trim();
            if (!message) return;

            // show user bubble
            const userMsg = document.createElement('div');
            userMsg.className = 'chat-message user';
            userMsg.textContent = message;
            chatBody.appendChild(userMsg);
            chatBody.scrollTop = chatBody.scrollHeight;
            chatInput.value = '';

            try {
                const response = await fetch(getChatUrl(), {
                    method: 'POST',
                    headers: {
                        'Content-Type' : 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken'  : document
                                         .querySelector('meta[name="csrf-token"]')
                                         .getAttribute('content'),
                    },
                    body: JSON.stringify({ message })
                });

                // اگر 200 نہ ملے تو بھی gracefully handle کریں
                if (!response.ok) {
                    throw new Error(`Server returned ${response.status}`);
                }

                const data = await response.json();
                const botMsg = document.createElement('div');
                botMsg.className = 'chat-message bot';
                botMsg.textContent = data.response || '…';
                chatBody.appendChild(botMsg);
                chatBody.scrollTop = chatBody.scrollHeight;

            } catch (err) {
                console.error('Chat error:', err);
                const errMsg = document.createElement('div');
                errMsg.className = 'chat-message bot';
                errMsg.textContent = 'Sorry, something went wrong.';
                chatBody.appendChild(errMsg);
            }
        };

        chatSend.addEventListener('click', (e) => {
            e.preventDefault();
            sendMessage();
        });

        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendMessage();
            }
        });
    }
});

// Newsletter
document.addEventListener('DOMContentLoaded', function () {

    // ✅ Get CSRF token from cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // ✅ Newsletter form submission handler
    const newsletterForm = document.querySelector('.newsletter-form');
    if (!newsletterForm) return;

    newsletterForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const emailInput = this.querySelector('input[name="email"]');
        if (!emailInput || !emailInput.value || !emailInput.checkValidity()) {
            alert("Please enter a valid email.");
            emailInput.focus();
            return;
        }

        const payload = { email: emailInput.value };

        fetch('/api/subscribe/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify(payload),
        })
        .then(async (res) => {
            const data = await res.json();
            if (res.ok && data.email) {
                this.innerHTML = `<div style="color:white;">Thank you for subscribing, ${data.email}</div>`;
            } else if (data.email && Array.isArray(data.email)) {
                alert(data.email[0]);
                emailInput.focus();
            } else if (data.detail) {
                alert(data.detail);
            } else {
                alert('Subscription failed. Please try again.');
            }
        })
        .catch(() => {
            alert('Something went wrong. Please try again later.');
        });
    });

});



// blog table of content


document.addEventListener('DOMContentLoaded', function () {
  const tocToggle = document.getElementById("toc-toggle");
  const tocList = document.getElementById("toc-list");
  const tocIcon = document.getElementById("toc-icon");

  // Check all elements exist before applying toggle
  if (tocToggle && tocList && tocIcon) {
    tocToggle.addEventListener("click", function () {
      if (tocList.style.display === "none" || tocList.style.display === "") {
        tocList.style.display = "block";
        tocIcon.textContent = "▲";
      } else {
        tocList.style.display = "none";
        tocIcon.textContent = "▼";
      }
    });
  }
});
