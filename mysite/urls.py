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
from django.urls import path, include
from django.contrib.auth import views as auth_views  # 👈 add this
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from newsletter.views import NewsletterSubscriptionViewSet

# REST Framework router for API endpoints
router = DefaultRouter()

router.register(r'subscribe', NewsletterSubscriptionViewSet, basename='newsletter')

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('careers/', include('careers.urls')),
    path('accounts/', include('accounts.urls')),
    path('quotes/', include('quotes.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('payments/', include('payments.urls')),
    path('portal/', include('client_portal.urls')),
    path('support/', include('support.urls')),
    path('kb/', include('knowledge_base.urls')),
    path('analytics/', include('analytics.urls')),
    path('localization/', include('localization.urls')),

    path('api/', include(router.urls)),


    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    