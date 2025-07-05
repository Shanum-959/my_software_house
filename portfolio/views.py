from django.shortcuts import render, get_object_or_404
from .models import (
    PortfolioProject,
    Hero,
    OverviewSection,
    RequirementsSection,
    SolutionsSection,
    ResultSection,
    FullWidthImage,
    TechnologySection
)

def portfolio_list(request):
    projects = PortfolioProject.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})


def portfolio_detail(request, slug):
    project = get_object_or_404(PortfolioProject, slug=slug)

    hero = Hero.objects.first()
    overview = OverviewSection.objects.first()
    requirements = RequirementsSection.objects.first()
    solutions = SolutionsSection.objects.first()
    result = ResultSection.objects.first()
    full_image = FullWidthImage.objects.first()
    tech_section = TechnologySection.objects.prefetch_related('technologies').first()

    context = {
        'project': project,
        'hero': hero,
        'overview': overview,
        'requirements': requirements,
        'solutions': solutions,
        'result': result,
        'full_image': full_image,
        'tech_section': tech_section,
    }

    return render(request, 'portfolio/portfolio_detail.html', context)
