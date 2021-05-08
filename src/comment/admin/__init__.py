from django.contrib import admin
from .comment import CommentAdmin
from comment.models.comment import Comment


admin.site.register(Comment, CommentAdmin)
