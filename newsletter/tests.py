from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Subscriber

class NewsletterSubscriptionAPITest(APITestCase):
    def setUp(self):
        self.subscribe_url = reverse('newsletter-list')  # DRF router ke according "basename-list"

    def test_successful_subscription(self):
        data = {'email': 'testuser@example.com'}
        response = self.client.post(self.subscribe_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertEqual(Subscriber.objects.first().email, 'testuser@example.com')

    def test_duplicate_subscription(self):
        Subscriber.objects.create(email='testuser@example.com')
        data = {'email': 'testuser@example.com'}
        response = self.client.post(self.subscribe_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(Subscriber.objects.count(), 1)

    def test_subscription_without_email(self):
        data = {}
        response = self.client.post(self.subscribe_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
