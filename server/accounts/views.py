from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Представление для создания нового пользователя"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDataApiView(APIView):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user_id = request.user.id
        username = request.user.username
        email = request.user.email

        response_data = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "message": "Hello, token-authenticated user!"
        }

        return Response(response_data)
