# example app/urls.py

from django.urls import path
from . import views
app_name = 'careers'
urlpatterns = [
    path('', views.careers_list, name='careers_home'),
]