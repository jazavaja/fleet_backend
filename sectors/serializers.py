from rest_framework import serializers

from sectors.models import ActivityCategory
from usages.models import UsageType


class ActivityCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityCategory
        fields = ['id', 'name', 'category_type', 'is_active']

