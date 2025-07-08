from django.shortcuts import render, get_object_or_404
from .models import (
    PortfolioProject,
    Hero,
    OverviewSection,
    RequirementsSection,
    SolutionsSection,
    ResultSection,
    FullWidthImage,
    TechnologySection,
)


def portfolio_list(request):
    projects = PortfolioProject.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})

def portfolio_detail(request, slug):
    project = get_object_or_404(PortfolioProject, slug=slug)

    hero = getattr(project, 'hero', None)
    tech_section = getattr(project, 'technology_section', None)

    # Agar multiple ho sakte hain but ek hi dikhana chah rahe ho
    overview_section = project.overview_sections.first()
    requirements_section = project.requirements_sections.first()
    solutions_section = project.solutions_sections.first()
    result_section = project.result_sections.first()
    full_image = project.fullwidth_images.first()

    context = {
        'project': project,
        'hero': hero,
        'overview': overview_section,
        'requirements': requirements_section,
        'solutions': solutions_section,
        'result': result_section,
        'full_image': full_image,
        'tech_section': tech_section,
        'technologies': tech_section.technologies.all() if tech_section else [],
    }

    return render(request, 'portfolio/portfolio_detail.html', context)
