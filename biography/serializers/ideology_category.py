from biography.models import IdeologyCategory
from rest_framework import serializers


class IdeologyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeologyCategory
        fields = '__all__'
