from rest_framework import serializers

from biography.models import IdeologyCategory


class IdeologyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeologyCategory
        fields = '__all__'
