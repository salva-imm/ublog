from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
