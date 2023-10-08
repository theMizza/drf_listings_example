from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Представление для создания нового пользователя"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDataApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        return Response({'data': UserSerializer(request.user).data})
