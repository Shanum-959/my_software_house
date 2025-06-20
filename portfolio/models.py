from django.db import models

class PortfolioProject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    client_name = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    project_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
