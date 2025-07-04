from django.urls import path
from . import views
app_name = 'careers'
urlpatterns = [
    path('', views.careers_list_view, name='careers-list'),
    path('<int:pk>/', views.career_detail_view, name='career-detail'),
]
