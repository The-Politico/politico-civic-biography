from rest_framework import serializers

from biography.models import Occupation


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'
