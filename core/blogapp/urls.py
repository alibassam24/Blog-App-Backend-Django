from rest_framework.urls import path, urlpatterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import create_user, login_user

urlpatterns = [
    path("create-user/", create_user, name="create-user"),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("login-user/", login_user, name="login-user"),
]
