from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityCategoryViewSet

router = DefaultRouter()
router.register(r'', ActivityCategoryViewSet, basename='activity-category')

urlpatterns = [
    path('', include(router.urls)),
]