from django.db import models

# Create your models here.
from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='core/logos/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('github', 'GitHub'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, help_text="FontAwesome icon class, e.g., 'fab fa-facebook'")

    def __str__(self):
        return self.platform


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=100)
    favicon = models.ImageField(upload_to='core/favicons/')
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    is_maintenance_mode = models.BooleanField(default=False)

    def __str__(self):
        return self.site_title
