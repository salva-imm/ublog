from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(
        max_length=512,
        verbose_name="Name"
    )
    slug = models.SlugField(
        max_length=512,
        allow_unicode=True,
        verbose_name="Slug"
    )
    image = models.ImageField(
        upload_to="category",
        verbose_name="Image"
    )
    short_description = models.CharField(
        max_length=512,
        verbose_name="Short description",
        null=True,
        blank=True
    )
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.SET_NULL,
        verbose_name="Parent category",
        null=True,
        blank=True
    )
    color = models.CharField(
        max_length=128,
        verbose_name="Color",
        null=True,
        blank=True
    )
