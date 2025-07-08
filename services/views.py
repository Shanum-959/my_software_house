from django.shortcuts import render, get_object_or_404
from .models import Service, Hero, About, FeatureSection, PlatformSection, ProcessSection, FAQ  # FAQ model bhi import karen

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

def services_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    
    hero = getattr(service, 'hero_section', None)
    about = getattr(service, 'about_section', None)
    feature_section = service.feature_sections.prefetch_related('features').first()
    platform_section = service.platform_sections.prefetch_related('platforms').first()
    process_section = service.process_sections.prefetch_related('steps').first()
    faqs = service.faqs.all()  # service ke related FAQs
    
    context = {
        'service': service,
        'hero': hero,
        'about': about,
        'feature_section': feature_section,
        'features': feature_section.features.all() if feature_section else [],
        'platform_section': platform_section,
        'process_section': process_section,
        'faqs': faqs,
    }
    return render(request, 'services/services_detail.html', context)
