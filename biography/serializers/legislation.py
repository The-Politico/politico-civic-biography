from rest_framework import serializers

from biography.models import Legislation


class LegislationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legislation
        fields = '__all__'
