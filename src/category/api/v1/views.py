from rest_framework import generics
from rest_framework.response import Response
from .serializers import CategoriesSerializer

from category.models.category import Category


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent=None).prefetch_related('translations')
    serializer_class = CategoriesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = list(map(lambda x: x.translated, queryset))
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)
