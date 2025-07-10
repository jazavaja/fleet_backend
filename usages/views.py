from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from usages.models import UsageType
from usages.serializers import UsageTypeSerializer


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class UsageTypeViewSet(viewsets.ModelViewSet):
    queryset = UsageType.objects.all()
    serializer_class = UsageTypeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
