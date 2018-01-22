from biography.models import Financials
from rest_framework import serializers


class FinancialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financials
        exclude = ('biography',)
