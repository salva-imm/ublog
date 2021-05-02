from django.contrib import admin
from .category import CategoryAdmin
from category.models.category import Category


admin.site.register(Category, CategoryAdmin)
