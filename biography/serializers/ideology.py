from rest_framework import serializers

from biography.models import Ideology


class IdeologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideology
        fields = '__all__'
