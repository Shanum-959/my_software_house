# example app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.knowledge, name='knowledge_base-home'),
]
