from django.urls import path
from .views import home_view, about_view, contact_list, contact_success



urlpatterns = [
    path('', home_view, name='home'),
    path('about/',about_view, name='about' ),

    path('contact/', contact_list, name='contact_form'),
    path('success/', contact_success, name='contact_success'),
]