from biography.models import Quote
from biography.serializers import QuoteSerializer

from .base import BaseViewSet


class QuoteViewSet(BaseViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
