from django.db import models
from django_extensions.db.models import TimeStampedModel


class CommentLike(TimeStampedModel):
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        verbose_name="User"
    )
    comment = models.ForeignKey(
        "comment.Comment",
        on_delete=models.CASCADE,
        verbose_name="Comment"
    )
