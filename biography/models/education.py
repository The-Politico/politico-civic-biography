from django.db import models
from entity.fields import CountryField, StateField

from biography.fields import MarkdownField


class Education(models.Model):
    ASSOCIATE = 'a'
    BACHELORS = 'b'
    MASTERS = 'm'
    DOCTORAL = 'd'
    OTHER = 'o'
    DEGREE_CHOICES = (
        (ASSOCIATE, "Associate degree"),
        (BACHELORS, "Bachelor's degree"),
        (MASTERS, "Master's degree"),
        (DOCTORAL, "Doctoral degree"),
        (OTHER, "Other")
    )

    biography = models.ForeignKey(
        'Biography',
        related_name="education",
        on_delete=models.CASCADE,
    )
    school = models.CharField(max_length=250)
    degree = models.CharField(
        max_length=1, choices=DEGREE_CHOICES, blank=True, null=True)
    honorary = models.BooleanField(default=False)
    state = StateField(blank=True, null=True)
    country = CountryField(default='US')
    notes = MarkdownField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(
            self.biography.person.full_name,
            self.school
        )

    class Meta:
        verbose_name_plural = "education"
