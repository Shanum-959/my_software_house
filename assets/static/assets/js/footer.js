document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('newsletter-form');
  const message = document.getElementById('newsletter-message');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('newsletter-email').value;

    try {
      const response = await fetch('/newsletter/subscribe/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();
      if (response.ok) {
        message.innerText = 'Please check your email to confirm subscription.';
        form.reset();
      } else {
        message.innerText = data.error || 'Subscription failed.';
      }
    } catch (err) {
      message.innerText = 'An error occurred.';
    }
  });

  // Helper to get CSRF token
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
