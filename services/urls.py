from django.urls import path
from . import views
app_name = 'services'
urlpatterns = [
    path('', views.service_list, name='services_home'),
    path('<slug:slug>/', views.services_detail, name='services_detail'),
]
