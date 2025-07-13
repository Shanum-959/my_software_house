from django.test import TestCase, Client
from django.urls import reverse
from .models import BlogPost, BlogSection
from django.utils.text import slugify

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog = BlogPost.objects.create(
            title="My First Blog",
            author="Fatima Azeemi",
            category="Tech",
            content="This is a sample blog post content."
        )
        self.section = BlogSection.objects.create(
            blog=self.blog,
            heading_id="intro",
            heading_title="Introduction",
            content="This is the intro section.",
            order=1
        )

    def test_blog_str_method(self):
        self.assertEqual(str(self.blog), "My First Blog")

    def test_blog_slug_auto_generated(self):
        self.assertEqual(self.blog.slug, slugify("My First Blog"))

    def test_blog_section_str(self):
        expected = f"{self.blog.title} - {self.section.heading_title}"
        self.assertEqual(str(self.section), expected)

    def test_blog_list_view_status_code(self):
        response = self.client.get(reverse('blog:blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My First Blog")

    def test_blog_list_view_search_query(self):
        response = self.client.get(reverse('blog:blog_home'), {'q': 'sample'})
        self.assertContains(response, "My First Blog")

    def test_blog_list_view_category_filter(self):
        response = self.client.get(reverse('blog:blog_home'), {'category': 'Tech'})
        self.assertContains(response, "My First Blog")

    def test_blog_detail_view_status_code(self):
        response = self.client.get(reverse('blog:blog_detail', args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My First Blog")

    def test_blog_detail_invalid_slug(self):
        response = self.client.get(reverse('blog:blog_detail', args=["non-existent"]))
        self.assertEqual(response.status_code, 404)
