from rest_framework.urls import path, urlpatterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

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
    path("view-blogs-by-user/", view_blogs_by_user, name="view-blogs-by-user"),
    path("create-comment/", create_comment, name="create-comment"),
    path(
        "view-comments-on-blog/<int:blog_id>/",
        view_comments_on_blog,
        name="view-comments-on-blog",
    ),
    path(
        "update-comment/<int:id>/",
        update_comment,
        name="update-comment",
    ),
    path(
        "delete-comment/<int:id>/",
        delete_comment,
        name="delete-comment",
    ),
]
