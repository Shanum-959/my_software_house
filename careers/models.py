from django.db import models

JOB_TYPES = (
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Internship', 'Internship'),
    ('Contract', 'Contract'),
)

WORK_MODES = (
    ('Remote', 'Remote'),
    ('Onsite', 'Onsite'),
    ('Hybrid', 'Hybrid'),
)

class Career(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    work_mode = models.CharField(max_length=20, choices=WORK_MODES)
    description = models.TextField()
    requirements = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
