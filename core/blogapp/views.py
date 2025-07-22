from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .serializers import BlogSerializer, CreateUserSerializer

# Create your views here.


# Api to create a user
@api_view(["POST"])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
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
            status=status.HTTP_400_BAD_REQUEST,
        )
