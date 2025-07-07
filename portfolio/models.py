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

class Hero(models.Model):
    background_image = models.ImageField(upload_to='hero/')

    def __str__(self):
        return "Hero Section"

class OverviewSection(models.Model):
    title = models.CharField(max_length=100, default="Overview")
    description = models.TextField()
    image = models.ImageField(upload_to='overview/')

    def __str__(self):
        return self.title

class RequirementsSection(models.Model):
    title = models.CharField(max_length=100, default="Requirements")
    description = models.TextField()
    image = models.ImageField(upload_to='requirements/')

    def __str__(self):
        return self.title

class SolutionsSection(models.Model):
    title = models.CharField(max_length=100, default="Solutions", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='solutions/')

    def __str__(self):
        return self.title or "Solutions Section"

class FullWidthImage(models.Model):
    image = models.ImageField(upload_to='fullwidth/')

    def __str__(self):
        return f"Full Image ID: {self.id}"

class ResultSection(models.Model):
    title = models.CharField(max_length=100, default="Result", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Result Section"

class TechnologySection(models.Model):
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
