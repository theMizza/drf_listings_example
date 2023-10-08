from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import CreateUserView, UserDataApiView


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('user/', UserDataApiView.as_view(), name='user_data'),
    path('token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify_token')
]