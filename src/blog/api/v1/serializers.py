from rest_framework import serializers
from blog.models.blog import Blog
from blog.models.content_list import ContentList


class BlogSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['author', 'banner_image', 'title', 'short_description', 'source_title', 'source_link', 'slug',
                  'keywords', 'meta_title', 'meta_description', 'canonical_tag', 'content', 'likes']


class ContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentList
        fields = '__all__'


class BlogWithContentsListSerializer(serializers.ModelSerializer):
    contents_list = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['author', 'banner_image', 'title', 'short_description', 'source_title', 'source_link', 'slug',
                  'keywords', 'meta_title', 'meta_description', 'canonical_tag', 'likes', 'contents_list']

    def get_contents_list(self, model):
        return ContentListSerializer(model.contents_list.all(), many=True).data
