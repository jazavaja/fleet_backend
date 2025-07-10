from django.urls import path
from . import views

urlpatterns = [
    path('provinces/', views.get_provinces, name='get_provinces'),
    path('cities/', views.get_cities, name='get_cities'),
    path('areas/', views.activity_area_list, name='activity_area_list'),
    path('areas/<int:pk>/', views.activity_area_detail, name='activity_area_detail'),
]