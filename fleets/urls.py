# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NavyTypeViewSet, NavySizeViewSet, NavyBrandViewSet, NavyMainViewSet, NavyMehvarViewSet, \
    GetMehvarsBySizeView, GetBrandsBySize, GetSizesByType

router = DefaultRouter()
router.register(r'types', NavyTypeViewSet, basename='navy-type')
router.register(r'sizes', NavySizeViewSet, basename='navy-size')
router.register(r'brands', NavyBrandViewSet, basename='navy-brand')
router.register(r'mehvars', NavyMehvarViewSet, basename='navy-mehvar')
router.register(r'main', NavyMainViewSet, basename='navy-main')

urlpatterns = [
    path('', include(router.urls)),
    path('sizes/by-type/<int:type_id>/', GetSizesByType.as_view(), name='sizes-by-type'),
    path('brands/by-size/<int:size_id>/', GetBrandsBySize.as_view(), name='brands-by-size'),
    path('mehvars/by-size/<int:size_id>/', GetMehvarsBySizeView.as_view(), name='brands-by-size')
]