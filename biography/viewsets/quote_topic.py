from biography.models import QuoteTopic
from biography.serializers import QuoteTopicSerializer

from .base import BaseViewSet


class QuoteTopicViewSet(BaseViewSet):
    queryset = QuoteTopic.objects.all()
    serializer_class = QuoteTopicSerializer
