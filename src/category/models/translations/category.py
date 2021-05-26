from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel


class CategoryTranslation(TimeStampedModel):
    language = models.CharField(
        max_length=64,
        verbose_name="Language",
        choices=settings.SUPPORTED_LANGUAGES
    )
    category = models.ForeignKey(
        to="category.Category",
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name="Category"
    )
    name = models.CharField(
        max_length=512,
        verbose_name="Name"
    )
    slug = models.SlugField(
        max_length=512,
        allow_unicode=True,
        verbose_name="Slug"
    )
    short_description = models.CharField(
        max_length=512,
        verbose_name="Short description",
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ['language', 'category']

    def __str__(self):
        return f"{self.name}-{self.category.name}"
