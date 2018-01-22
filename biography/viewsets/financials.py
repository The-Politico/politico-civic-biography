from biography.models import Financials
from biography.serializers import FinancialsSerializer

from .base import BaseViewSet


class FinancialsViewSet(BaseViewSet):
    queryset = Financials.objects.all()
    serializer_class = FinancialsSerializer
