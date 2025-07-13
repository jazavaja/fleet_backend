from rest_framework import serializers

from fleets.models import NavyType, NavyMain, NavyBrand, NavySize


class NavyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavyType
        fields = ['id', 'name', 'logo']


class NavySizeSerializer(serializers.ModelSerializer):
    types = NavyTypeSerializer(many=True, read_only=True)
    type_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=NavyType.objects.all(), write_only=True, source='types'
    )

    class Meta:
        model = NavySize
        fields = ['id', 'name', 'logo', 'types', 'type_ids']


class NavyBrandSerializer(serializers.ModelSerializer):
    sizes = NavySizeSerializer(many=True, read_only=True)

    size_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=NavySize.objects.all(), write_only=True, source='sizes'
    )

    class Meta:
        model = NavyBrand
        fields = ['id', 'name', 'logo', 'sizes', 'size_ids']


class NavyMainSerializer(serializers.ModelSerializer):
    type = NavyTypeSerializer(read_only=True)
    size = NavySizeSerializer(read_only=True)
    brand = NavyBrandSerializer(read_only=True)

    type_id = serializers.PrimaryKeyRelatedField(
        queryset=NavyType.objects.all(), source='type', write_only=True, required=False
    )
    size_id = serializers.PrimaryKeyRelatedField(
        queryset=NavySize.objects.all(), source='size', write_only=True, required=False
    )
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=NavyBrand.objects.all(), source='brand', write_only=True, required=False
    )

    class Meta:
        model = NavyMain
        fields = ['id', 'name', 'type', 'size', 'brand', 'type_id', 'size_id', 'brand_id', 'tip']
