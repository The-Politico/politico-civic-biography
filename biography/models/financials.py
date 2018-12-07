from django.db import models


class Financials(models.Model):
    biography = models.OneToOneField(
        "Biography", related_name="financials", on_delete=models.CASCADE
    )

    net_worth = models.DecimalField(max_digits=14, decimal_places=2)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "financials"

    def __str__(self):
        return self.biography.person.full_name
