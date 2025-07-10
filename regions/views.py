from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Province, City, ActivityArea
from .serializers import ProvinceSerializer, CitySerializer, ActivityAreaSerializer

@api_view(['GET'])
def get_provinces(request):
    provinces = Province.objects.all()
    serializer = ProvinceSerializer(provinces, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_cities(request):
    province_id = request.GET.get('province_id')
    if not province_id:
        return JsonResponse({'error': 'province_id is required'}, status=400)
    cities = City.objects.filter(province_id=province_id)
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def activity_area_list(request):
    if request.method == 'GET':
        areas = ActivityArea.objects.all()
        serializer = ActivityAreaSerializer(areas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("Received data:", request.data)
        serializer = ActivityAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def activity_area_detail(request, pk):
    try:
        area = ActivityArea.objects.get(pk=pk)
    except ActivityArea.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = ActivityAreaSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        area.delete()
        return Response(status=204)