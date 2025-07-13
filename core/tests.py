from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage

class ContactFormTests(TestCase):

    def test_contact_form_display(self):
        """Check that the contact form page loads correctly."""
        response = self.client.get(reverse('contact_form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your Name')
        self.assertContains(response, 'Your Email')
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_form_submission_success(self):
        """Test submitting a valid contact form."""
        form_data = {
            'name': 'Fatima Azeemi',
            'email': 'fatima@example.com',
            'phone': '03001234567',
            'company_name': 'Shams Peak Salt',
            'message': 'I want to know more about your services.',
        }
        response = self.client.post(reverse('contact_form'), data=form_data)
        self.assertEqual(response.status_code, 302)  # should redirect to success
        self.assertRedirects(response, reverse('contact_success'))

        # Check if the message was saved
        self.assertEqual(ContactMessage.objects.count(), 1)
        message = ContactMessage.objects.first()
        self.assertEqual(message.name, 'Fatima Azeemi')

    def test_contact_success_view(self):
        """Ensure the success page renders correctly."""
        response = self.client.get(reverse('contact_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')
