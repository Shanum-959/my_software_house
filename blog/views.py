from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.db.models import Q
# from django.views.decorators.cache import cache_page

# @cache_page(60 * 15)
def blog_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    blogs = BlogPost.objects.all().order_by('-published_at')

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    if category:
        blogs = blogs.filter(category__iexact=category)

    categories = BlogPost.objects.values_list('category', flat=True).distinct()

    return render(request, 'blog/blog.html', {
        'blogs': blogs,
        'categories': categories,
    })



def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    # Get 3 latest blog posts excluding the current one
    recent_posts = BlogPost.objects.exclude(id=post.id).order_by('-published_at')[:3]

    return render(request, 'blog/blog_list.html', {
        'post': post,
        'recent_posts': recent_posts,
    })