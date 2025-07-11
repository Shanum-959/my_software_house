from django.contrib import admin
from .models import BlogPost, BlogSection

class BlogSectionInline(admin.TabularInline):
    model = BlogSection
    extra = 1

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogSectionInline]
    prepopulated_fields = {'slug': ('title',)}

