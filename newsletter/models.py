from django.db import models
from django.utils import timezone

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    confirmation_token = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
