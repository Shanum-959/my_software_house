from django.contrib import admin
from .models import Career

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'category', 'job_type', 'work_mode', 'posted_at')
    search_fields = ('title', 'location', 'category')
