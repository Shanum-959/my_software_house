"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
import os

from newsletter.views import NewsletterSubscriptionViewSet
from django.contrib.sitemaps.views import sitemap
from mysite.sitemaps import (
    BlogSitemap,
    CareerSitemap,
    PortfolioSitemap,
    ServiceSitemap,
    StaticViewSitemap,
)

# REST Framework router for newsletter API
router = DefaultRouter()
router.register(r'subscribe', NewsletterSubscriptionViewSet, basename='newsletter')

# Sitemap dictionary for various apps
sitemaps = {
    'blog': BlogSitemap,
    'careers': CareerSitemap,
    'portfolio': PortfolioSitemap,
    'services': ServiceSitemap,
    'static': StaticViewSitemap,
}

# error handling

from django.conf.urls import handler400, handler403, handler404, handler500
from django.shortcuts import render

def custom_400(request, exception):
    return render(request, '400.html', status=400)

def custom_403(request, exception):
    return render(request, '403.html', status=403)

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

handler400 = custom_400
handler403 = custom_403
handler404 = custom_404
handler500 = custom_500


urlpatterns = [
    # Core app urls (home, about, contact etc.)
    path('', include('core.urls')),

    # Admin panel
    path('admin/', admin.site.urls),

    # App specific urls
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('careers/', include('careers.urls', namespace='careers')),
    path('chatbot/', include('chatbot.urls')),

    # API urls from REST Framework router
    path('api/', include(router.urls)),

    # Sitemap url
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Password reset confirm url
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
]

# Static and media files serving in development mode
if settings.DEBUG:
    # Serve media files uploaded by users
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Serve robots.txt from static folder without template rendering
    urlpatterns += [
        re_path(r'^robots\.txt$', serve, {
            'path': 'robots.txt',
            'document_root': os.path.join(settings.BASE_DIR, 'assets/static'),  # Path to your static folder
            'content_type': 'text/plain',
        }),
    ]
