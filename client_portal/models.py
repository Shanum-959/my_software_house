from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100)
    deadline = models.DateField()

    def __str__(self):
        return self.name

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='client_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



