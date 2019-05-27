from uuid import uuid4

from django.contrib.auth import authenticate, logout, login
from django.db.models.functions import Lower
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from user.serializers import AuthorCreateSerializer, AuthorLoginSerializer, \
    UniqueEmailSerializer, UniqueUsernameSerializer
from user.models import Author


class AuthorRegisterView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        serializer = AuthorCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AuthorLoginSerializer

    @staticmethod
    def post(request):
        author = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"),
        )
        if author is None or not author.is_active:
            return Response({
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)
        # login(request, author)
        author.token = uuid4()
        author.save()
        return Response(AuthorLoginSerializer(author).data)


class LogoutView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, author_id=None):
        author = Author.objects.filter(id=author_id).first()
        if author:
            author.token = None
            author.save()
            return Response(
                AuthorLoginSerializer(author).data,
                status=status.HTTP_204_NO_CONTENT
            )
        request.user.token = None
        request.user.save()
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class CheckToken(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.query_params.get('token', None)
        if not token:
            return Response(
                {'error': 'Add token in query parameters, like ?token=your_token'},
                status=status.HTTP_400_BAD_REQUEST
            )
        author = Author.objects.filter(token=token)

        if author.exists():
            return Response(AuthorLoginSerializer(author.first()).data)

        return Response(
            {'error': 'This token doesn\'t exist'},
            status=status.HTTP_400_BAD_REQUEST
        )


class CheckUniqueEmail(APIView):
    permission_classes = [AllowAny]
    serializer_class = UniqueEmailSerializer

    def get(self, request):
        email = request.query_params.get('email', None)
        if not email:
            return Response({'error': 'Add email in query parameters, like ?email=email@email.com'})
        author_lower_email = Author.objects.annotate(lower_email=Lower('email'))
        author = author_lower_email.filter(lower_email=email)
        if author.exists():
            return Response({
                'email': email,
                'error': 'Account with this email already exists'
            })
        return Response(UniqueEmailSerializer(request.query_params).data)


class CheckUniqueUsername(APIView):
    permission_classes = [AllowAny]
    serializer_class = UniqueUsernameSerializer

    def get(self, request):
        username = request.query_params.get('username', None)
        if not username:
            return Response({'error': 'Add username in query parameters, like ?username=your_username'})
        author_lower_username = Author.objects.annotate(lower_username=Lower('username'))
        author = author_lower_username.filter(lower_username=username.lower())
        if author.exists():
            return Response({
                'username': username,
                'error': 'Account with this username already exists'
            })
        return Response(UniqueUsernameSerializer(request.query_params).data)
