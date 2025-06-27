# newsletter/models.py
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)  # ✅ Add this field

    def __str__(self):
        return self.email
