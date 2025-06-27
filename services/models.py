from django.db import models
from django.contrib.auth.models import User  # Needed for user field

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Use icon class like 'fa-solid fa-code'")
    image = models.ImageField(upload_to='services/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

# ✅ Add this below
class OrderedService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordered_services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.title}"
