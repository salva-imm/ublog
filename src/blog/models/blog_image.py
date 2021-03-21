from django.db import models
from django_extensions.db.models import TimeStampedModel
class BlogImage(TimeStampedModel):
    image = models.ImageField(
        upload_to="blog_image",
        verbose_name="Blog image"
    )
    thumbnail = models.ImageField(
        upload_to="blog_image_thumbnail",
        verbose_name="Thumbnail"
    )
    description = models.CharField(
        max_length=256,
        verbose_name="Description"
    )
