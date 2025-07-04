from django.contrib import admin
from .models import (
    Service, Hero, About, FeatureSection, Feature,
    PlatformSection, Platform,
    ProcessSection, ProcessStep,
    FAQ,
    OrderedService
)

# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('created_at',)

# Hero Admin
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('heading',)

# About Admin
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading',)

# Feature Inline for FeatureSection
class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

# FeatureSection Admin with Inline Features
@admin.register(FeatureSection)
class FeatureSectionAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    inlines = [FeatureInline]

# Platform Inline for PlatformSection
class PlatformInline(admin.TabularInline):
    model = Platform
    extra = 1

# PlatformSection Admin with Inline Platforms
@admin.register(PlatformSection)
class PlatformSectionAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    inlines = [PlatformInline]

# ProcessStep Inline for ProcessSection
class ProcessStepInline(admin.TabularInline):
    model = ProcessStep
    extra = 1
    fields = ('step_number', 'title', 'description', 'icon', 'image', 'icon_svg')
    ordering = ('step_number',)

# ProcessSection Admin with Inline Steps
@admin.register(ProcessSection)
class ProcessSectionAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    inlines = [ProcessStepInline]

# Standalone ProcessStep Admin
@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'section')
    list_filter = ('section',)
    search_fields = ('title', 'description')
    ordering = ('section', 'step_number')


# FAQ Admin
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)
