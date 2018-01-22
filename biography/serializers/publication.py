from biography.models import Publication
from rest_framework import serializers


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        exclude = ('biography',)
