from rest_framework import serializers
from .models import MLModel
from .models import User

class YourMLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = ['id', 'file', 'name']  # example fields




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password']

