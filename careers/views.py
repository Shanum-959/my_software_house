from django.shortcuts import render, get_object_or_404
from .models import Career
from django.db.models import Q

def careers_list_view(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    careers = Career.objects.all()

    if query:
        careers = careers.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query)
        )

    if category:
        careers = careers.filter(category__iexact=category)

    categories = Career.objects.values_list('category', flat=True).distinct()

    return render(request, 'careers/careers.html', {
        'careers': careers,
        'categories': categories,
    })

def career_detail_view(request, pk):
    career = get_object_or_404(Career, pk=pk)
    return render(request, 'careers/career-detail.html', {'career': career})
