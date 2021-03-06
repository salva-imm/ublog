from django.db import models
from django_extensions.db.models import TimeStampedModel


class ContentList(TimeStampedModel):
    CONTENT_TYPES = (
        ("file", "file"),
        ("text", "text")
    )
    content_type = models.CharField(
        max_length=128,
        verbose_name="Content type",
        choices=CONTENT_TYPES
    )
    blog = models.ForeignKey(
        "blog.Blog",
        on_delete=models.CASCADE,
        related_name="contents_list",
        verbose_name="Blog"
    )
    file = models.ForeignKey(
        "file.File",
        verbose_name="File",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    text = models.TextField(
        verbose_name="Text",
        null=True,
        blank=True
    )
