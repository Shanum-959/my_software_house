from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import (
    PortfolioProject, OverviewSection, RequirementsSection,
    SolutionsSection, ResultSection, FullWidthImage,
    TechnologySection, Technology
)

class PortfolioViewsTestCase(TestCase):
    def setUp(self):
        self.project = PortfolioProject.objects.create(
            title="AI Dashboard",
            slug="ai-dashboard",
            client_name="TechCorp",
            description="A dashboard powered by AI for data insights.",
            image=SimpleUploadedFile(name='project.jpg', content=b'image_content', content_type='image/jpeg'),
            project_url="https://techcorp.com"
        )

        OverviewSection.objects.create(
            project=self.project,
            title="Project Overview",
            description="Detailed overview of the AI dashboard.",
            image=SimpleUploadedFile(name='overview.jpg', content=b'image_content', content_type='image/jpeg')
        )

        RequirementsSection.objects.create(
            project=self.project,
            title="Project Requirements",
            description="List of project requirements.",
            image=SimpleUploadedFile(name='requirements.jpg', content=b'image_content', content_type='image/jpeg')
        )

        SolutionsSection.objects.create(
            project=self.project,
            title="Our Solution",
            description="The solution we provided.",
            image=SimpleUploadedFile(name='solution.jpg', content=b'image_content', content_type='image/jpeg')
        )

        ResultSection.objects.create(
            project=self.project,
            title="Results",
            description="Results of the implementation."
        )

        FullWidthImage.objects.create(
            project=self.project,
            image=SimpleUploadedFile(name='full.jpg', content=b'image_content', content_type='image/jpeg')
        )

        tech_section = TechnologySection.objects.create(
            project=self.project,
            heading="Tech Stack",
            description="We used Django, React, and PostgreSQL."
        )

        Technology.objects.create(
            section=tech_section,
            name="Django",
            icon=SimpleUploadedFile(name='django.png', content=b'image_content', content_type='image/png')
        )

    def test_portfolio_list_view(self):
        url = reverse('portfolio:portfolio_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AI Dashboard")

    def test_portfolio_detail_view(self):
        url = reverse('portfolio:portfolio_detail', kwargs={'slug': self.project.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project Overview")
        self.assertContains(response, "Our Solution")
        self.assertContains(response, "Tech Stack")
