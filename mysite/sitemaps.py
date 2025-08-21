from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost
from careers.models import Career
from portfolio.models import PortfolioProject
from services.models import Service

# Blog Sitemap
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.published_at  # updated_at nahi to published_at use karo

# Careers Sitemap
class CareerSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        # Filter only objects with slug
        return Career.objects.exclude(slug='')

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.posted_at


# Portfolio Sitemap
from datetime import datetime

class PortfolioSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return PortfolioProject.objects.all()

    def lastmod(self, obj):
        return datetime.now()


# Services Sitemap
class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        # updated_at agar exist kare to use karo, warna created_at
        return getattr(obj, 'updated_at', obj.created_at)

    def location(self, obj):
        return reverse("services:services_detail", kwargs={"slug": obj.slug})



# Static Pages Sitemap (core pages, newsletter etc.)
class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return ['home', 'about', 'contact_form']

    def location(self, item):
        return reverse(item)