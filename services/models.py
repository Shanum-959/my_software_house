from django.db import models
from django.contrib.auth.models import User  # Needed for user field

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, null=True, blank=True, help_text="Use icon class like 'fa-solid fa-code'")
    icon_svg = models.TextField(
        null=True,
        blank=True,
        help_text="Paste complete SVG code here (starting with <svg...>)"
    )
    image = models.ImageField(upload_to='services/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Hero(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    background_image = models.ImageField(upload_to='hero_images/')

    def __str__(self):
        return self.heading
    
class About(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.heading

class FeatureSection(models.Model):
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading

class Feature(models.Model):
    feature_section = models.ForeignKey(
        FeatureSection,
        related_name='features',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_svg = models.TextField(
        null=True,
        blank=True,
        help_text="Paste complete SVG code here"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PlatformSection(models.Model):
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading

class Platform(models.Model):
    platform_section = models.ForeignKey(
        PlatformSection,
        related_name='platforms',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='platforms/logos/')

    def __str__(self):
        return self.name

class ProcessSection(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Process Section Settings"

class ProcessStep(models.Model):
    section = models.ForeignKey(ProcessSection, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, null=True, blank=True, help_text="Use icon class like 'fa-solid fa-code'")
    image = models.ImageField(upload_to='process/images/', blank=True, null=True)
    icon_svg = models.TextField(
        null=True,
        blank=True,
        help_text="Paste complete SVG code here"
    )
    
    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


# ✅ Add this below
class OrderedService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordered_services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.title}"