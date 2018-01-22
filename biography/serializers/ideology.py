from biography.models import Ideology
from rest_framework import serializers


class IdeologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideology
        exclude = ('biography',)
