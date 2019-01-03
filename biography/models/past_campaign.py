from django.db import models
from government.models import Office


class PastCampaign(models.Model):
    """
    A notable previous campaign
    """

    biography = models.ForeignKey(
        "Biography", related_name="campaigns", on_delete=models.CASCADE
    )
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    notes = models.TextField(blank=True, null=True)
