from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'parent', 'blog', 'likes', 'is_validated']
