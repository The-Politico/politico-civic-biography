from biography.fields import MarkdownField
from django.db import models
from entity.models import Person


class Biography(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.person.full_name

    class Meta:
        verbose_name_plural = "biographies"
