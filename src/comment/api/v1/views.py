from rest_framework import generics
from rest_framework.response import Response
from .serializers import CommentsSerializer

from comment.models.comment import Comment
# from blog.models.content_list import ContentList


class GetCommentsView(generics.ListAPIView):
    queryset = Comment.objects.filter(is_validated=False)
    serializer_class = CommentsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentCreateView:
    pass


class CommentDeleteView:
    pass


class CommentEditView:
    pass
