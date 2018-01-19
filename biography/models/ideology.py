from django.db import models


class IdeologyCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ideology categories"


class Ideology(models.Model):
    biography = models.OneToOneField(
        'Biography',
        related_name="ideology",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(IdeologyCategory, on_delete=models.PROTECT)

    dw_nominate = models.DecimalField(
        max_digits=4, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return self.biography.person.full_name

    class Meta:
        verbose_name_plural = 'ideology'
