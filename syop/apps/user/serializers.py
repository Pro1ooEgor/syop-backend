from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from user.models import Author


class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "email",
            "username",
            "password"
        ]
    extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        author = Author.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return author


class AuthorLoginSerializer(ModelSerializer):
    class Meta:
        model = Author
        exclude = ('password',)


class UniqueEmailSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'email'
        ]


class UniqueUsernameSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'username'
        ]
