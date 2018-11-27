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
    organization = models.ForeignKey(
        Organization,
        related_name="+",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Optionally, associate this occupation with an organization.",
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.biography.person.full_name, self.title)
