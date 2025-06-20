# example app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_portal-home'),
]
