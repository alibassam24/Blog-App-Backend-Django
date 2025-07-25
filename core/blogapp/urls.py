from rest_framework.urls import path, urlpatterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path("create-user/", create_user, name="create-user"),
    # path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("login-user/", login_user, name="login-user"),
    # path("logout-user/",logout_user,name="logout-user"),
    path("create-blog/", create_blog, name="create-blog"),
    path("view-blogs/", view_blogs, name="view-blogs"),
    path("delete-blog/<int:id>/", delete_blog, name="delete-blog"),
    path("search-blogs/", search_blogs, name="search-blogs"),
    path("update-blog/<int:id>", update_blog, name="update-blog"),
]
