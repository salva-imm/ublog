from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


class CategoryTranslationAdmin(admin.ModelAdmin):
    list_display = ['language', 'category', 'name']
