from rest_framework import serializers

from fleets.models import NavyType, NavyMain, NavyBrand, NavySize
from sectors.models import ActivityCategory
from usages.models import UsageType


class NavyTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavyType
        fields = ['id', 'name','logo']


class NavySizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavySize
        fields = ['id', 'name','logo']


class NavyBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavyBrand
        fields = ['id', 'name','logo']


class NavyMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavyMain
        fields = ['id', 'name']