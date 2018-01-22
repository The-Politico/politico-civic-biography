from biography.models import Education
from rest_framework import serializers


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('biography',)
