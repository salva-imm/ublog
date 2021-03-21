from django.db import models
from django_extensions.db.models import TimeStampedModel


class Blog(TimeStampedModel):
    author = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Author"
    )
    banner_image = models.ForeignKey(
        "blog.BlogImage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Banner image"
    )
    title = models.CharField(
        max_length=256,
        verbose_name="Title"
    )
    short_description = models.CharField(
        max_length=512,
        verbose_name="Short description",
        null=True,
        blank=True
    )
    source_title = models.CharField(
        max_length=512,
        verbose_name="Source title",
        null=True,
        blank=True
    )
    source_link = models.TextField(
        verbose_name="Source link",
        null=True,
        blank=True
    )
    slug = models.SlugField(
        allow_unicode=True,
        max_length=512,
        verbose_name="Slug",
    )
    keywords = models.TextField(
        verbose_name="Keywords",
    )
    meta_title = models.TextField(
        verbose_name="Meta title",
    )
    meta_description = models.TextField(
        verbose_name="Meta description",
    )
    canonical_tag = models.TextField(
        verbose_name="Canonical tag",
    )
    content = models.TextField(
        verbose_name="Content",
    )
    likes = models.PositiveIntegerField(
        verbose_name="Likes",
        default=0
    )
