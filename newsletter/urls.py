# example app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_list, name='newsletter-home'),
]
