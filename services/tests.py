from django.test import TestCase
from django.urls import reverse
from .models import Service, FAQ, FeatureSection, Feature, PlatformSection, Platform, ProcessSection, ProcessStep, Hero, About
from django.core.files.uploadedfile import SimpleUploadedFile

class ServiceViewsTestCase(TestCase):

    def setUp(self):
        self.service = Service.objects.create(
            title="Custom Software Development",
            slug="custom-software-development",
            description="We build scalable software.",
        )

        Hero.objects.create(
            service=self.service,
            heading="Build Your Dream Software",
            subheading="We turn ideas into reality",
            background_image=SimpleUploadedFile(
                name='hero.jpg',
                content=b'file_content',
                content_type='image/jpeg'
            )
        )

        About.objects.create(
            service=self.service,
            heading="About Our Service",
            content="We offer full-stack development.",
            image=SimpleUploadedFile(
                name='about.jpg',
                content=b'file_content',
                content_type='image/jpeg'
            )
        )

        feature_section = FeatureSection.objects.create(service=self.service, heading="Features")
        Feature.objects.create(
            feature_section=feature_section,
            title="Scalable Architecture",
            description="Built to grow with your business."
        )

        platform_section = PlatformSection.objects.create(service=self.service, heading="Platforms")
        Platform.objects.create(
            platform_section=platform_section,
            name="Web",
            logo=SimpleUploadedFile(
                name='logo.png',
                content=b'file_content',
                content_type='image/png'
            )
        )

        process_section = ProcessSection.objects.create(service=self.service, heading="Our Process")
        ProcessStep.objects.create(
            section=process_section,
            step_number=1,
            title="Consult",
            description="Understand your goals"
        )

        FAQ.objects.create(
            service=self.service,
            question="What technologies do you use?",
            answer="We use Django, React, etc."
        )

    def test_service_list_view(self):
        url = reverse('services:services_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/services.html')
        self.assertContains(response, self.service.title)

    def test_service_detail_view(self):
        url = reverse('services:services_detail', args=[self.service.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/services_detail.html')
        self.assertContains(response, self.service.title)
        self.assertContains(response, "Scalable Architecture")  # Feature title
        self.assertContains(response, "What technologies do you use?")  # FAQ




