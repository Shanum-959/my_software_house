from django.urls import path
from . import views

app_name = 'client_portal'

urlpatterns = [
    path('', views.dashboard_view, name='basic'),
    path('client/', views.client_portal_home, name='client_portal-home'),
    path('project/<int:pk>/', views.project_detail_view, name='project_detail'),
]
