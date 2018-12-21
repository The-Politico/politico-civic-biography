from biography.fields import MarkdownField
from django.db import models
from entity.models import Organization


class Occupation(models.Model):
    """
    Jobs.
    """

    PRIVATE = "private"
    PUBLIC = "public"
    GOVERNMENT = "government"
    MILITARY = "military"
    SECTOR_CHOICES = (
        (PRIVATE, "Private"),
        (GOVERNMENT, "Public - Government"),
        (MILITARY, "Public - Military"),
        (PUBLIC, "Public - Other"),
    )

    biography = models.ForeignKey(
        "Biography", related_name="occupations", on_delete=models.CASCADE
    )
    sector = models.CharField(
        max_length=10, choices=SECTOR_CHOICES, default=PRIVATE
    )
    title = models.CharField(max_length=250)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    present = models.BooleanField(default=False)
    employer = models.CharField(max_length=250, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.biography.person.full_name, self.title)
