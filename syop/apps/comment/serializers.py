from rest_framework import serializers

from comment.models import Comment
from user.serializers import AuthorLoginSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorLoginSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
