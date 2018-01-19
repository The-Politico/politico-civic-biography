from rest_framework import serializers

from biography.models import Birthplace


class BirthplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birthplace
        fields = '__all__'
