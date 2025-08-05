from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Career
from django.db.models import Q
from django.contrib import messages
from .forms import JobApplicationForm


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

def career_detail_view(request, slug):
    career = get_object_or_404(Career, slug=slug)

    ai_features = [
        {'feature': 'Resume Parser', 'endpoint': '/api/parse_resume/', 'status': '✅'},
        {'feature': 'Relevance Matching', 'endpoint': '/api/match_score/', 'status': '⏳'},
        {'feature': 'Smart Job Suggestions', 'endpoint': '/api/recommend_jobs/', 'status': '⏳'},
        {'feature': 'Interview Bot', 'endpoint': '/api/interview/', 'status': '⏳'},
        {'feature': 'Sentiment Analysis', 'endpoint': '/api/sentiment/', 'status': '⏳'},
        {'feature': 'CV Quality Checker', 'endpoint': '/api/cv_quality/', 'status': '⏳'},
    ]

    return render(request, 'careers/career-detail.html', {
        'career': career,
        'ai_features': ai_features,
    })
def apply_view(request, slug):
    career = get_object_or_404(Career, slug=slug)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.career = career
            application.save()
            messages.success(request, 'Your application has been submitted successfully.')
            return redirect('careers:career-detail', slug=career.slug)  
        else:
            messages.error(request, 'Please fill all the errors below.') # You can change this to a success page
        # Add this line:
            return render(request, 'careers/apply.html', {'form': form, 'career': career})
    else:
        form = JobApplicationForm()
    return render(request, 'careers/apply.html', {'form': form, 'career': career})