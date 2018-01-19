from rest_framework import serializers

from biography.models import Financials


class FinancialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financials
        fields = '__all__'
