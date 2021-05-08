from django.contrib import admin


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'slug', 'likes', 'is_draft']
