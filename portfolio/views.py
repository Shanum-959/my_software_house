from django.shortcuts import render
from .models import PortfolioProject

def portfolio_list(request):
    projects = PortfolioProject.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
