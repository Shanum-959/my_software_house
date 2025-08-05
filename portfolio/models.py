from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class PortfolioProject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    client_name = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    project_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class OverviewSection(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name='overview_sections')
    title = models.CharField(max_length=100, default="Overview")
    description = models.TextField()
    image = models.ImageField(upload_to='overview/')

    def __str__(self):
        return self.title

class RequirementsSection(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name='requirements_sections')
    title = models.CharField(max_length=100, default="Requirements")
    description = models.TextField()
    image = models.ImageField(upload_to='requirements/')

    def __str__(self):
        return self.title

class SolutionsSection(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name='solutions_sections')
    title = models.CharField(max_length=100, default="Solutions", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='solutions/')

    def __str__(self):
        return self.title or "Solutions Section"

class FullWidthImage(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name='fullwidth_images')
    image = models.ImageField(upload_to='fullwidth/')

    def __str__(self):
        return f"Full Image ID: {self.id}"

class ResultSection(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name='result_sections')
    title = models.CharField(max_length=100, default="Result", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Result Section"

class TechnologySection(models.Model):
    project = models.OneToOneField(PortfolioProject, on_delete=models.CASCADE, related_name='technology_section')
    heading = models.CharField(max_length=100, default="Our Technology Stack")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading

class Technology(models.Model):
    section = models.ForeignKey(TechnologySection, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='tech_icons/')

    def __str__(self):
        return self.name
