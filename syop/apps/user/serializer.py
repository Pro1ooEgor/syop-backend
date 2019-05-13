from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Author


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Author.objects.create_user(
            password=make_password(
                validated_data['user'].pop('password')
            ),
            **validated_data.pop('user')
        )

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            instance.user.password = make_password(
                validated_data.get('user').get('password', instance.user.password)
            )
            instance.user.save()

    class Meta:
        model = Author
        fields = (
            'login', 'email', 'first_name', 'last_name'
        )
