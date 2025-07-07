from django.contrib import admin
from .models import Career
from .models import JobApplication

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'category', 'job_type', 'work_mode', 'posted_at')
    search_fields = ('title', 'location', 'category')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'career', 'email', 'submitted_at')
    search_fields = ('full_name', 'email', 'career__title')