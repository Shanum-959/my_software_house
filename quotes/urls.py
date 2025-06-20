from django.urls import path
from . import views

urlpatterns = [
    path('', views.qoutes_list, name='quotes'),
]
