from biography.models import Publication
from biography.serializers import PublicationSerializer

from .base import BaseViewSet


class PublicationViewSet(BaseViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
