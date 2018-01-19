from biography.models import (Birthplace, Education, Financials, Ideology,
                              Legislation, Occupation, Publication)
from django.contrib import admin


class BirthplaceInline(admin.TabularInline):
    model = Birthplace


class FinancialsInline(admin.TabularInline):
    model = Financials


class IdeologyInline(admin.TabularInline):
    model = Ideology


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0


class OccupationInline(admin.StackedInline):
    model = Occupation
    extra = 0


class PublicationInline(admin.StackedInline):
    model = Publication
    extra = 0


class LegislationInline(admin.StackedInline):
    model = Legislation
    extra = 0


class BiographyAdmin(admin.ModelAdmin):
    inlines = [
        BirthplaceInline,
        FinancialsInline,
        IdeologyInline,
        EducationInline,
        OccupationInline,
        PublicationInline,
        LegislationInline,
    ]
