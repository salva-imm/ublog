from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
