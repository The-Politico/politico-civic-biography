from biography.fields import MarkdownField
from django.db import models


class Legislation(models.Model):
    """
    Legislative achievements.
    """

    SPONSOR = "sponsor"
    COSPONSOR = "cosponsor"
    SIGNATORY = "signatory"
    ROLE_OPTIONS = (
        (SPONSOR, "Sponsor"),
        (COSPONSOR, "Cosponsor"),
        (SIGNATORY, "Signatory"),
    )

    biography = models.ForeignKey(
        "Biography", related_name="legislation", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=500)
    topic = models.CharField(max_length=250)
    role = models.CharField(
        blank=True, null=True, max_length=10, choices=ROLE_OPTIONS
    )
    passage_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Legislative accomplishments"
