# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NavyTypeViewSet, NavySizeViewSet, NavyBrandViewSet, NavyMainViewSet

router = DefaultRouter()
router.register(r'types', NavyTypeViewSet, basename='navy-type')
router.register(r'sizes', NavySizeViewSet, basename='navy-size')
router.register(r'brands', NavyBrandViewSet, basename='navy-brand')
router.register(r'main', NavyMainViewSet, basename='navy-main')

urlpatterns = [
    path('', include(router.urls)),
]