from django.contrib import admin


class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file_type']
