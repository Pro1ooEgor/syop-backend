from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from comment.models import Comment
from comment.serializers import CommentSerializer, CreateCommentSerializer


class CommentList(APIView):
    """
    List all articles, or create a new article.
    """
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Comment.objects.filter(article_id=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, title_pk, format=None):
        comment = self.get_object(title_pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request, title_pk, format=None):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
