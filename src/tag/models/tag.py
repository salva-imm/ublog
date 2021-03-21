from django.db import models
from django_extensions.db.models import TimeStampedModel


class Tag(TimeStampedModel):
    name = models.CharField(
        max_length=512,
        verbose_name="Name"
    )
