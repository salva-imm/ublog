from django.contrib import admin
from .category import CategoryAdmin, CategoryTranslationAdmin
from category.models.category import Category
from category.models.translations.category import CategoryTranslation


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryTranslation, CategoryTranslationAdmin)
