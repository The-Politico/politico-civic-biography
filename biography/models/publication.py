from biography.fields import MarkdownField
from django.db import models


class Publication(models.Model):
    """
    Published works, authored, co-authored or ghost-written.
    """

    BOOK = "book"
    ARTICLE = "article"
    OTHER = "other"
    PUBLICATION_TYPES = (
        (BOOK, "Book"),
        (ARTICLE, "Article"),
        (OTHER, "Other"),
    )

    biography = models.ForeignKey(
        "Biography", related_name="publications", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=500)
    publication_type = models.CharField(
        max_length=10, choices=PUBLICATION_TYPES, default=BOOK
    )
    publication_date = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=250, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.biography.person.full_name, self.title)

    class Meta:
        verbose_name_plural = "Published works"
