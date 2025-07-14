# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NavyTypeViewSet, NavySizeViewSet, NavyBrandViewSet, NavyMainViewSet, get_sizes_by_type, \
    get_brands_by_size

router = DefaultRouter()
router.register(r'types', NavyTypeViewSet, basename='navy-type')
router.register(r'sizes', NavySizeViewSet, basename='navy-size')
router.register(r'brands', NavyBrandViewSet, basename='navy-brand')
router.register(r'main', NavyMainViewSet, basename='navy-main')

urlpatterns = [
    path('', include(router.urls)),
    path('sizes/by-type/<int:type_id>/', get_sizes_by_type, name='sizes-by-type'),
    path('brands/by-size/<int:size_id>/', get_brands_by_size, name='brands-by-size')
]