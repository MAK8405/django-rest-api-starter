# This file tell python how to transform our model into JSON data that we can access in our API.
# The class in line 6 created for the purpose of top comment.
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
