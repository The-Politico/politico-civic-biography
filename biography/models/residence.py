from django.db import models
from entity.fields import CountryField, StateField


class Residence(models.Model):
    biography = models.OneToOneField(
        "Biography", related_name="residence", on_delete=models.CASCADE
    )

    city = models.CharField(max_length=250, blank=True, null=True)
    state = StateField(blank=True, null=True)
    country = CountryField(default="US")

    def __str__(self):
        return self.biography.person.full_name

    class Meta:
        verbose_name_plural = "residence"
