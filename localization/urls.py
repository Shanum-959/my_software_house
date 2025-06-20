# example app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.localization_list, name='localization-home'),
]
