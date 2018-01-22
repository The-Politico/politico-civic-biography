from biography.models import Ideology
from biography.serializers import IdeologySerializer

from .base import BaseViewSet


class IdeologyViewSet(BaseViewSet):
    queryset = Ideology.objects.all()
    serializer_class = IdeologySerializer
