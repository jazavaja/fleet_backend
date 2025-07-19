# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import PermissionRequired, ModelPermissionMap
from fleets.models import NavyType, NavyBrand, NavyMain, NavySize, NavyMehvar
from fleets.permissions import FleetPermissions
from fleets.serializers import NavySizeSerializer, NavyTypeSerializer, NavyMainSerializer, NavyBrandSerializer, \
    NavyMehvarSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 200


class NavyTypeViewSet(viewsets.ModelViewSet):
    queryset = NavyType.objects.all()
    serializer_class = NavyTypeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated,ModelPermissionMap]


class NavySizeViewSet(viewsets.ModelViewSet):
    queryset = NavySize.objects.all()
    serializer_class = NavySizeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated,ModelPermissionMap]


class NavyBrandViewSet(viewsets.ModelViewSet):
    queryset = NavyBrand.objects.all()
    serializer_class = NavyBrandSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated,ModelPermissionMap]


class NavyMehvarViewSet(viewsets.ModelViewSet):
    queryset = NavyMehvar.objects.all()
    serializer_class = NavyMehvarSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated,ModelPermissionMap]


class NavyMainViewSet(viewsets.ModelViewSet):
    queryset = NavyMain.objects.all()
    serializer_class = NavyMainSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsAuthenticated, ModelPermissionMap]


class GetSizesByType(APIView):
    permission_classes = [PermissionRequired(FleetPermissions.VIEW_NAVYSIZE)]

    def get(self, request, type_id):
        try:
            type_instance: NavyType = NavyType.objects.get(id=type_id)
            sizes = type_instance.sizes.all()  # related_name in NavySize.types
            serializer = NavySizeSerializer(sizes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NavyType.DoesNotExist:
            return Response({'error': 'NavyType not found'}, status=status.HTTP_404_NOT_FOUND)


class GetBrandsBySize(APIView):
    permission_classes = [PermissionRequired(FleetPermissions.VIEW_NAVYBRAND)]

    def get(self, request, size_id):
        try:
            size_instance: NavySize = NavySize.objects.get(id=size_id)
            brands = size_instance.brands.all()  # related_name in NavyBrand.sizes
            serializer = NavyBrandSerializer(brands, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NavySize.DoesNotExist:
            return Response({'error': 'NavySize not found'}, status=status.HTTP_404_NOT_FOUND)


class GetMehvarsBySizeView(APIView):
    permission_classes = [PermissionRequired(FleetPermissions.VIEW_NAVYMEHVAR)]

    def get(self, request, size_id):
        try:
            size_instance: NavySize = NavySize.objects.get(id=size_id)
            mehvars = size_instance.mehvars.all()
            serializer = NavyMehvarSerializer(mehvars, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NavySize.DoesNotExist:
            return Response({'error': 'NavySize not found'}, status=status.HTTP_404_NOT_FOUND)
