from rest_framework import serializers

from usages.models import UsageType


class UsageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsageType
        fields = ['id', 'name', 'description']

