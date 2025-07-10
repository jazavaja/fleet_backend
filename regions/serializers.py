from rest_framework import serializers

from .models import Province, City, ActivityArea


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name', 'slug', 'tel_prefix']


class CitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'name', 'slug', 'province', 'county_id']


class ActivityAreaSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city',
        write_only=True
    )
    class Meta:
        model = ActivityArea
        fields = ['id', 'city','city_id', 'area']
