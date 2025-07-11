from django.contrib import admin
from .models import (
    PortfolioProject,
    OverviewSection,
    RequirementsSection,
    SolutionsSection,
    FullWidthImage,
    ResultSection,
    TechnologySection,
    Technology
)

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'client_name')

@admin.register(OverviewSection)
class OverviewAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(RequirementsSection)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(SolutionsSection)
class SolutionsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(FullWidthImage)
class FullWidthImageAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(ResultSection)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1

@admin.register(TechnologySection)
class TechnologySectionAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    inlines = [TechnologyInline]

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')
    list_filter = ('section',)
    search_fields = ('name',)
