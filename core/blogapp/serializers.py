from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from .models import Blog, User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields='__all__'
        fields = ["username", "age", "bio", "email"]
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
        fields = "__all__"
        read_only_fields = ["id", "author_id", "created_at", "updated_at"]
