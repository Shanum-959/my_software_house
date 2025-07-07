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
    qualifications = models.TextField(blank=True)  # <-- add this line
    posted_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    career = models.ForeignKey('Career', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.career.title}"