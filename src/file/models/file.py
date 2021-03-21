from django.db import models
from django_extensions.db.models import TimeStampedModel


class File(TimeStampedModel):
    file = models.FileField(
        upload_to="files",
        verbose_name="File"
    )
    name = models.CharField(
        max_length=512,
        verbose_name="Name"
    )
    file_type = models.CharField(
        max_length=128,
        verbose_name="File type"
    )
