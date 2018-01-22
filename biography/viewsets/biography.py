from biography.models import Biography
from biography.serializers import BiographySerializer

from .base import BaseViewSet


class BiographyViewSet(BaseViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
