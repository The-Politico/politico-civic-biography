from biography.models import Occupation
from biography.serializers import OccupationSerializer

from .base import BaseViewSet


class OccupationViewSet(BaseViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
