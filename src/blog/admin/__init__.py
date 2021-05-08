from django.contrib import admin
from .blog import BlogAdmin
from blog.models.blog import Blog


admin.site.register(Blog, BlogAdmin)
