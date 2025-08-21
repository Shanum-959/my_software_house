from django.urls import path
from . import views
app_name = 'careers'
urlpatterns = [
    path('', views.careers_list_view, name='careers-list'),
    path('<slug:slug>/', views.career_detail_view, name='career-detail'),
    path('<slug:slug>/apply/', views.apply_view, name='career-apply'),

]
