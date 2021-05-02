from rest_framework import serializers
from category.models.category import Category


class CategoriesSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'slug', 'image', 'short_description', 'color', 'subcategories']

    def get_subcategories(self, model):
        return CategoriesSerializer(model.children.all(), many=True).data
