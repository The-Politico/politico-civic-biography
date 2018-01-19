from biography.fields import MarkdownField
from django.db import models
from uuslug import uuslug


class QuoteTopic(models.Model):
    """
    A topic a quote pertains to.
    """
    slug = models.SlugField(
        max_length=255, blank=True, null=True, editable=False)
    name = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        self.slug = uuslug(
            self.name,
            instance=self,
            max_length=100,
            separator='-',
            start_no=2
        )
        super(QuoteTopic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Quote(models.Model):
    """
    Quotes spoken.
    """
    biography = models.ForeignKey(
        'Biography',
        related_name="quotes",
        on_delete=models.CASCADE,
    )
    text = MarkdownField()
    topic = models.ForeignKey(
        'QuoteTopic', blank=True, null=True, on_delete=models.PROTECT)
    date = models.DateField()
    place = models.CharField(
        max_length=250, blank=True, null=True,
        help_text="If known, name the location where speaker spake.")
    link = models.URLField(
        blank=True, null=True,
        help_text="If available, add a link to the quote on social"
        " media or as published online.")
    context = MarkdownField(blank=True, null=True)

    @property
    def truncated(self):
        return ' '.join(self.text.split()[:10])

    @property
    def speaker(self):
        return self.biography.person.full_name

    def __str__(self):
        return self.biography.full_name
