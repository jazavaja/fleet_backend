from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsageTypeViewSet

router = DefaultRouter()
router.register(r'', UsageTypeViewSet, basename='usage-type')

urlpatterns = [
    path('', include(router.urls)),
]