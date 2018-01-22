from biography.models import Birthplace
from biography.serializers import BirthplaceSerializer

from .base import BaseViewSet


class BirthplaceViewSet(BaseViewSet):
    queryset = Birthplace.objects.all()
    serializer_class = BirthplaceSerializer
