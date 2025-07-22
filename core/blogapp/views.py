from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import UserSerializer,BlogSerializer
from rest_framework.response import Response
# Create your views here.


#Api to create a user 
@api_view(['POST'])
def create_user(request):
    serializer= UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Success","Message":"User Created","Data": serializer.data})
    else:
        return Response({"Status":"Failed","Message":"Invalid Data"})