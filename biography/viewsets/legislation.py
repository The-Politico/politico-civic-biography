from biography.models import Legislation
from biography.serializers import LegislationSerializer

from .base import BaseViewSet


class LegislationViewSet(BaseViewSet):
    queryset = Legislation.objects.all()
    serializer_class = LegislationSerializer
