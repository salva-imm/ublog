from django.db import models
from django_extensions.db.models import TimeStampedModel


class Comment(TimeStampedModel):
    author = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        verbose_name="Author"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Parent category",
        null=True,
        blank=True
    )
    blog = models.ForeignKey(
        "blog.Blog",
        on_delete=models.CASCADE,
        verbose_name="Blog"
    )
    content = models.TextField(
        verbose_name="Content"
    )
    likes = models.PositiveIntegerField(
        default=0,
        verbose_name="Likes"
    )
