from django.shortcuts import render, get_object_or_404
from .models import Service, Hero, About, FeatureSection, PlatformSection, ProcessSection, FAQ  # FAQ model bhi import karen

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

def services_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    hero = Hero.objects.first()
    about = About.objects.first()
    feature_section = FeatureSection.objects.prefetch_related('features').first()
    platform_section = PlatformSection.objects.prefetch_related('platforms').first()
    process_section = ProcessSection.objects.prefetch_related('steps').first()
    
    faqs = FAQ.objects.all()  # FAQ objects fetch kar rahe hain

    context = {
        'service': service,
        'hero': hero,
        'about': about,
        'feature_section': feature_section,
        'features': feature_section.features.all() if feature_section else [],
        'platform_section': platform_section,
        'process_section': process_section,
        'faqs': faqs,  # context mein faqs add kar rahe hain
    }
    return render(request, 'services/services_detail.html', context)