# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from fleets.models import NavyType, NavyBrand, NavyMain, NavySize
from fleets.serializers import NavySizeSerializer, NavyTypeSerializer, NavyMainSerializer, NavyBrandSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class NavyTypeViewSet(viewsets.ModelViewSet):
    queryset = NavyType.objects.all()
    serializer_class = NavyTypeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]


class NavySizeViewSet(viewsets.ModelViewSet):
    queryset = NavySize.objects.all()
    serializer_class = NavySizeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]


class NavyBrandViewSet(viewsets.ModelViewSet):
    queryset = NavyBrand.objects.all()
    serializer_class = NavyBrandSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]

class NavyMainViewSet(viewsets.ModelViewSet):
    queryset = NavyMain.objects.all()
    serializer_class = NavyMainSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]
