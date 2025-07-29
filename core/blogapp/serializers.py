from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from .models import Blog, Comment, User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        # fields = ["username", "age", "bio", "email"]
        read_only_fields = ["id"]

    def validate(self, data):
        age = data.get("age", 0)
        username = data.get("username", "").lower()
        bio = data.get("bio", "").lower()
        email = data.get("email", "").lower()

        if age < 18:
            raise serializers.ValidationError("User must be 18 or above")
        if username == User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists")
        if not bio:
            raise serializers.ValidationError("Bio cannot be empty")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return data


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        #  fields = ["title","content"]
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, data):
        # id = .objects.get("id", "")
        content = data.get("content", "")
        title = data.get("title", "")
        if not title:
            raise serializers.ValidationError("Title cannot be empty")
        if not content:
            raise serializers.ValidationError("Blog cannot be empty")
        if Blog.objects.filter(content=content).exists():
            raise serializers.ValidationError("Blog already exists")
        return data


class UpdateBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ["title", "content"]

    def validate(self, data):
        content = data.get("content", "")
        title = data.get("title", "")
        if not title:
            raise serializers.ValidationError("Title cannot be empty")
        if not content:
            raise serializers.ValidationError("Blog cannot be empty")
        return data


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "blog", "content"]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, data):
        user = data.get("user")
        blog = data.get("blog")
        comment_content = data.get("content", "")
        # if not isinstance(user,User):      <--------------Handled already by model serializer--------------->
        # raise serializers.ValidationError("User does not exist")
        # if not isinstance(blog,Blog):
        #       raise serializers.ValidationError("Blog Does not Exist")
        if not comment_content:
            raise serializers.ValidationError("Comment cannot be empty")
        return data


class ViewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["content", "user"]
        read_only_fields = ["created_at", "updated_at", "blog"]


class UpdateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["content"]
        read_only_fields = ["created_at", "updated_at", "blog", "user"]

    def validate(self, data):
        if not data.get("content"):
            raise serializers.ValidationError("Comment cannot be empty")

        return data
