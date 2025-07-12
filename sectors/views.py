# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from sectors.models import ActivityCategory
from sectors.serializers import ActivityCategorySerializer


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class ActivityCategoryViewSet(viewsets.ModelViewSet):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]
