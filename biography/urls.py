from django.urls import include, path
from rest_framework import routers

from .viewsets import (BiographyViewSet, BirthplaceViewSet, EducationViewSet,
                       FinancialsViewSet, IdeologyCategoryViewSet,
                       IdeologyViewSet, LegislationViewSet, OccupationViewSet,
                       PublicationViewSet, QuoteTopicViewSet, QuoteViewSet)

router = routers.DefaultRouter()

router.register(r'biographies', BiographyViewSet)
router.register(r'birthplaces', BirthplaceViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'financials', FinancialsViewSet)
router.register(r'ideology-categories', IdeologyCategoryViewSet)
router.register(r'ideologies', IdeologyViewSet)
router.register(r'legislation', LegislationViewSet)
router.register(r'occupations', OccupationViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'quote-topics', QuoteTopicViewSet)
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
