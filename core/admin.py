from django.contrib import admin
from .models import CompanyInfo, SocialLink, SiteSetting
from .models import ContactMessage

admin.site.register(CompanyInfo)
admin.site.register(SocialLink)
admin.site.register(SiteSetting)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company_name', 'created_at')
    search_fields = ('name', 'email', 'company_name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
