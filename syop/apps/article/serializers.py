from rest_framework import serializers

from article.models import Article
from user.serializers import AuthorLoginSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorLoginSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
