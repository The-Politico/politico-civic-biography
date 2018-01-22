from biography.models import Biography
from rest_framework import serializers

from .birthplace import BirthplaceSerializer
from .education import EducationSerializer
from .financials import FinancialsSerializer
from .ideology import IdeologySerializer
from .legislation import LegislationSerializer
from .occupation import OccupationSerializer
from .publication import PublicationSerializer


class BiographySerializer(serializers.ModelSerializer):
    birthplace = BirthplaceSerializer()
    education = EducationSerializer(many=True)
    financials = FinancialsSerializer()
    ideology = IdeologySerializer()
    legislation = LegislationSerializer(many=True)
    occupations = OccupationSerializer(many=True)
    publications = PublicationSerializer(many=True)

    class Meta:
        model = Biography
        fields = (
            'person',
            'notes',
            'birthplace',
            'education',
            'financials',
            'ideology',
            'legislation',
            'occupations',
            'publications',
        )
