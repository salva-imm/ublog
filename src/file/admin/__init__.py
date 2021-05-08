from django.contrib import admin
from .file import FileAdmin
from file.models.file import File


admin.site.register(File, FileAdmin)
