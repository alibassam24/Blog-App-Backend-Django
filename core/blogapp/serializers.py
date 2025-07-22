from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User,Blog
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'
        read_only_fields=['id']

    def validate(self, data):
        age=data.get('age','')
        username=data.get('username','').lower()
        if age<18:
            return serializers.ValidationError("User must be 18 or above")
        if username in User.objects.get(username):
            return serializers.ValidationError("Username already exists")
        
        
        return data

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model=Blog
        fields='__all__'
        read_only_fields=['id','author_id','created_at','updated_at']

   