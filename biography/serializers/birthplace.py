from biography.models import Birthplace
from rest_framework import serializers


class BirthplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birthplace
        exclude = ('biography',)
