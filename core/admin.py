from django.contrib import admin
from .models import CompanyInfo, SocialLink, SiteSetting

admin.site.register(CompanyInfo)
admin.site.register(SocialLink)
admin.site.register(SiteSetting)
