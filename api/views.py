from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


@api_view(["GET"])
def get_user(request):
    return Response(UserSerializer({"name": "pedro", "age": 23}).data)
