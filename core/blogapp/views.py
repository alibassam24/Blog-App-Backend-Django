from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import *
from .serializers import (
    BlogSerializer,
    CreateCommentSerializer,
    CreateUserSerializer,
    UpdateBlogSerializer,
    UpdateCommentSerializer,
    ViewCommentSerializer,
)

# Create your views here.


# USER_________________________________________________________________________________________________________


# Api to create a user
@api_view(["POST"])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    password = request.data.get("password")
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(
            {"Status": "Success", "Message": "User Created", "Data": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(
            {"Status": "Failed", "Message": "Invalid Data", "Error": serializer.errors},
            status=status.HTTP_401_UNAUTHORIZED,
        )


# user login
@api_view(["POST"])
##not needed here@authentication_classes([JWTAuthentication])
def login_user(request):
    username = request.data.get("username", "")
    password = request.data.get("password", "")

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)
        return Response(
            {"refresh": str(refresh), "access": str(access)}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"Status": "Failed", "Message": "Invalid Credentials"},
            # status=status.HTTP_400_BAD_REQUEST,
        )


"""
session auth logout uses logout()
jwt logout functionality to be added 
 @api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def logout_user(request):
    logout(request)
    return Response({"Status":"Success","Message":"User logged out successfully"})

 """


##BLOGS_________________________________________________________________________________________________


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_blog(request):
    data = request.data.copy()
    data["author_id"] = request.user.id
    serializer = BlogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"Status": "Success", "Message": "Blog created", "Data": serializer.data},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"Status": "Failed", "Message": "Invalid Data", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_blogs(request):
    paginator = PageNumberPagination()
    blogs = Blog.objects.all()
    page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(page, many=True)

    if not blogs.exists():
        return Response(
            {"Status": "Failed", "Message": "No records found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    else:
        return paginator.get_paginated_response(
            {
                "Status": "Success",
                "Message": "All pages fetched",
                "Data": serializer.data,
            }
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_blog(request, id):
    if not id:
        return Response({"status": "failed", "message": "missing required fields"})
    try:
        blog = Blog.objects.get(id=id)
        if request.user.id == blog.author_id.id:
            blog.delete()
            return Response(
                {"Status": "Success", "Message": "Blog Deleted"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"Status": "Failed", "Message": "Permission Denied"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Blog.DoesNotExist:
        return Response(
            {"Status": "Failed", "Message": "Blog not found"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def search_blogs(request):
    title = request.GET.get("title", "")
    paginator = PageNumberPagination()
    blogs = Blog.objects.filter(title__icontains=title)
    if blogs.exists():
        page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(page, many=True)

        return paginator.get_paginated_response(
            {
                "Status": "Success",
                "Message": "Search Implemented",
                "Data": serializer.data,
            }
        )
        # return Response({"Status":"Success","Message":"Blog Found","Data":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"Status": "Failed", "Message": "Blog not found"})
        # return Response({"Status":"Failed","Message":"No blog with title exists"},status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_blogs_by_user(request):
    user = request.user.id
    if Blog.objects.filter(author_id=user).exists():
        blogs = Blog.objects.filter(author_id=user)
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(page, many=True)
        return paginator.get_paginated_response(
            {"Status": "Success", "Message": "Blog Found", "Data": serializer.data}
        )
    # return Response({"Status":"Success","Message":"blogs found","Data":serializer.data})
    else:
        return Response({"sttatus": "failed", "message": "no blogs exist"})


# if not title:
# blogs=Blog.objects.filter(title__icontains=title)
# serializer=BlogSerializer(blogs,many=True)
# if blogs.exists():
#   return Response({"Status":"Success","Message":"Blog Found","Data":serializer.data}, status=status.HTTP_200_OK)
# else:
#   return Response({"Status":"Failed","Message":"No blog with title exists"},status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def update_blog(request, id):
    try:
        blogs = Blog.objects.get(id=id)
        if blogs.author_id.id == request.user.id:
            title = request.data.get("title", "")
            if not title:
                return Response({"status": "failed", "message": "title missing"})

            content = request.data.get("content", "")
            if not content:
                return Response({"status": "failed", "message": "content missing"})
                # blogs.title = title
                # blogs.content = content
                # blogs.save()
                ## need to pass data with serializer too
            serializer = UpdateBlogSerializer(blogs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "Status": "Success",
                        "Message": "Blog updated",
                        "Data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "Status": "Failed",
                        "Message": "Invalid Data",
                        "Errors": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response({"Status": "Failed", "Message": "Permission Denied"})
    except Blog.DoesNotExist:
        return Response(
            {"Status": "Failed", "Message": "Blog not found"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# COMMENTS______________________________________________________________________________________________________


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request):
    serializer = CreateCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"Status": "Success  ", "Message": "Comment added", "Data": serializer.data}
        )
    else:
        return Response(
            {"Status": "Failed", "Message": "Invalid Data", "Errors": serializer.errors}
        )


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_comments_on_blog(request, blog_id):
    if not blog_id:
        return Response({"Status": "Failed", "Message": "Missing id"})
    else:
        try:
            blogs = Blog.objects.get(id=blog_id)
            comments = Comment.objects.filter(blog=blog_id)

            if comments.exists():
                commentSerializer = ViewCommentSerializer(comments, many=True)
                return Response(
                    {
                        "Status": "Success",
                        "Message": "Comments found",
                        "Comments": commentSerializer.data,
                    }
                )
            else:
                return Response({"Status": "Success", "Message": "No comments on blog"})
        except Blog.DoesNotExist:
            return Response({"Status": "Failed", "Message": "Blog not found"})


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_comment(request, id):
    try:
        comment = Comment.objects.get(id=id)
        if comment.user.id == request.user.id:
            comment.delete()
            return Response({"Status": "Success", "Message": "Comment Deleted"})
        else:
            return Response({"status": "failed", "Message": "permission denied"})
    except:
        return Response({"Status": "Failed", "Message": "Comment not found"})


@api_view(["PATCH"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_comment(request, id):

    try:
        comment = Comment.objects.get(id=id)
        if comment.user.id == request.user.id:
            comment.content = request.data.get("content", "")
            serializer = UpdateCommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "Status": "Success",
                        "Message": "Comment updated",
                        "Data": serializer.data,
                    }
                )
            else:
                return Response({"Status": "Failed", "Message": "Invalid Data"})
        else:
            return Response({"Status": "failed", "Message": "permission denied"})
    except Comment.DoesNotExist:
        return Response({"Status": "Falied", "Message": "Comment not found"})
