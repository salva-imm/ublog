from rest_framework import serializers
from comment.models.comment import Comment


class CommentsSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['author', 'blog', 'content', 'likes', 'is_validated', 'replies']

    def get_replies(self, model):
        return CommentsSerializer(model.replies.all(), many=True).data
