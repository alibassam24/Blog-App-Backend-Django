from django.shortcuts import render
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.response import Response

from .serializers import BlogSerializer, CreateUserSerializer
from rest_framework import status
# Create your views here.


#Api to create a user 
@api_view(['POST'])
def create_user(request):
    serializer= CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Success","Message":"User Created","Data": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({"Status":"Failed","Message":"Invalid Data","Error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
""""    
Test For create-user

{
    "username":"test",
    "email":"ali@gmail.com",
    "password":"123",
    "bio":"hello my name is ali and i love write articles",
    "age":"18"
}    
"""
"""
{
    "Status": "Success",
    "Message": "User Created",
    "Data": {
        "id": 2,
        "password": "123",
        "last_login": null,
        "is_superuser": false,
        "first_name": "",
        "last_name": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2025-07-22T05:21:06.243129Z",
        "username": "test",
        "email": "ali@gmail.com",
        "bio": "hello my name is ali and i love write articles",
        "age": 18,
        "groups": [],
        "user_permissions": []
    }
}
"""