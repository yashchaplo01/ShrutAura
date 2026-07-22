/**
 * ShrutAura Global - Analytics Tracking Implementation
 * Handles dataLayer pushes for custom events requested in Phase 4.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Ensure dataLayer exists
  window.dataLayer = window.dataLayer || [];

  /**
   * Helper function to push standardized events to GTM dataLayer
   * @param {string} eventName - The custom event name
   * @param {Object} eventParams - Additional custom parameters
   */
  const pushToDataLayer = (eventName, eventParams = {}) => {
    window.dataLayer.push({
      event: eventName,
      page_location: window.location.href,
      page_title: document.title,
      // country, device, traffic_source are generally handled by GA4 natively,
      // but we can pass them if explicitly defined in GTM variables.
      ...eventParams
    });
    console.log(`[Analytics] Event Tracked: ${eventName}`, eventParams);
  };

  /**
   * 1. Book Consultation (Hero CTA & About CTA)
   */
  const bookButtons = document.querySelectorAll('a[href="#contact"]');
  bookButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      // Check if it's actually the nav link vs CTA button
      if (btn.classList.contains('btn')) {
        pushToDataLayer('book_consultation', {
          button_text: btn.innerText.trim() || 'Book Consultation'
        });
      }
    });
  });

  /**
   * 2. WhatsApp Clicks
   */
  const whatsappLinks = document.querySelectorAll('a[href*="wa.me"]');
  whatsappLinks.forEach(link => {
    link.addEventListener('click', () => {
      pushToDataLayer('whatsapp_click', {
        button_text: link.innerText.trim() || 'WhatsApp Icon'
      });
    });
  });

  /**
   * 3. Email Clicks
   */
  const emailLinks = document.querySelectorAll('a[href^="mailto:"]');
  emailLinks.forEach(link => {
    link.addEventListener('click', () => {
      pushToDataLayer('email_click', {
        button_text: link.innerText.trim() || link.getAttribute('href')
      });
    });
  });

  /**
   * 4. Phone Clicks
   */
  const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
  phoneLinks.forEach(link => {
    link.addEventListener('click', () => {
      pushToDataLayer('phone_click', {
        button_text: link.innerText.trim() || 'Phone Link'
      });
    });
  });

  /**
   * 5. Service Inquiry & FAQ Toggle Tracking
   */
  const serviceCards = document.querySelectorAll('#services .card');
  serviceCards.forEach(card => {
    card.addEventListener('click', () => {
      const titleEl = card.querySelector('h3');
      const serviceName = titleEl ? titleEl.innerText.trim() : 'Unknown Service';
      pushToDataLayer('service_inquiry', {
        service_name: serviceName
      });
    });
  });

  const faqTriggers = document.querySelectorAll('.faq-trigger');
  faqTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const questionText = trigger.querySelector('.faq-question')?.innerText.trim() || 'FAQ Item';
      pushToDataLayer('faq_interaction', {
        question: questionText
      });
    });
  });

  /**
   * 6. Download Brochure
   */
  const downloadLinks = document.querySelectorAll('a[href$=".pdf"]');
  downloadLinks.forEach(link => {
    link.addEventListener('click', () => {
      pushToDataLayer('download_brochure', {
        button_text: link.innerText.trim() || 'Download PDF'
      });
    });
  });

  /**
   * 7. Calendly Booking Listener
   * Listens for the postMessage event sent by an embedded Calendly widget.
   */
  window.addEventListener('message', (e) => {
    if (e.data && e.data.event === 'calendly.event_scheduled') {
      pushToDataLayer('calendly_booking', {
        service_name: 'Consultation'
      });
    }
  });

  /**
   * 8. Contact Form Submit
   * (Bind this to your form's submit event when you build the form)
   */
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', () => {
      pushToDataLayer('contact_form_submit', {
        button_text: 'Submit Form'
      });
    });
  }
});
