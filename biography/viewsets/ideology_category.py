from biography.models import IdeologyCategory
from biography.serializers import IdeologyCategorySerializer

from .base import BaseViewSet


class IdeologyCategoryViewSet(BaseViewSet):
    queryset = IdeologyCategory.objects.all()
    serializer_class = IdeologyCategorySerializer
