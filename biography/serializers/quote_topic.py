from rest_framework import serializers

from biography.models import QuoteTopic


class QuoteTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteTopic
        fields = '__all__'
