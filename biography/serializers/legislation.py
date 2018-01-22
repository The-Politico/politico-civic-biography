from biography.models import Legislation
from rest_framework import serializers


class LegislationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legislation
        exclude = ('biography',)
