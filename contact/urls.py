from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_list, name='contact_form'),
    path('success/', views.contact_success, name='contact_success'),
]
