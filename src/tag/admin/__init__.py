from django.contrib import admin
from .tag import TagAdmin
from tag.models.tag import Tag


admin.site.register(Tag, TagAdmin)
