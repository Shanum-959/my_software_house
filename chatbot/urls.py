# example app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='Chatbot-home'),
]
