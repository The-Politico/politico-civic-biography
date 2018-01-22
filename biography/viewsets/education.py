from biography.models import Education
from biography.serializers import EducationSerializer

from .base import BaseViewSet


class EducationViewSet(BaseViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
