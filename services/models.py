from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, null=True, blank=True, help_text="Use icon class like 'fa-solid fa-code'")
    icon_svg = models.TextField(null=True, blank=True, help_text="Paste complete SVG code here (starting with <svg...>)")
    image = models.ImageField(upload_to='services/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title or "Unnamed Service"

    def get_absolute_url(self):
        return reverse("services:services_detail", kwargs={"slug": self.slug})
    
# 🔸 Hero Section
class Hero(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='hero_section')
    heading = models.CharField(max_length=200, blank=True, null=True)
    subheading = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    background_image = models.ImageField(upload_to='hero_images/')

    def __str__(self):
        return self.heading or f"Hero for {self.service.title}"

# 🔸 About Section
class About(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='about_section')
    heading = models.CharField(max_length=200)
    content = models.TextField()
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.heading or f"About for {self.service.title}"

# 🔸 Feature Section
class FeatureSection(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='feature_sections')
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading or f"Features for {self.service.title}"

class Feature(models.Model):
    feature_section = models.ForeignKey(FeatureSection, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_svg = models.TextField(null=True, blank=True, help_text="Paste complete SVG code here")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Unnamed Feature"

# 🔸 Platform Section
class PlatformSection(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='platform_sections')
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading or f"Platform Section for {self.service.title}"

class Platform(models.Model):
    platform_section = models.ForeignKey(PlatformSection, related_name='platforms', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='platforms/logos/')

    def __str__(self):
        return self.name or "Unnamed Platform"

# 🔸 Process Section
class ProcessSection(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='process_sections')
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.heading or f"Process for {self.service.title}"

class ProcessStep(models.Model):
    section = models.ForeignKey(ProcessSection, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, null=True, blank=True, help_text="Use icon class like 'fa-solid fa-code'")
    image = models.ImageField(upload_to='process/images/', blank=True, null=True)
    icon_svg = models.TextField(null=True, blank=True, help_text="Paste complete SVG code here")

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title or 'Untitled'}"

# 🔸 FAQ Section
class FAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question or "FAQ"

# 🔸 Ordered Service
class OrderedService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordered_services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.title}"
