from rest_framework import generics
from rest_framework.response import Response
from .serializers import BlogSerializer, BlogWithContentsListSerializer

from blog.models.blog import Blog
# from blog.models.content_list import ContentList


class BlogView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_draft=False)
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


class BlogWithContentsListView(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_draft=False)
    serializer_class = BlogWithContentsListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogWithContentsListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        pass  # TODO: create content and connect to blog table
