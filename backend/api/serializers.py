from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Animal

#Create UserSerializer class with fields for id, username and password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        #Ensure that password is write only so that the value isn't returned with username and id
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["id", "species", "name", "favorite_food", "added_to_zoo", "details", "photo", "zookeeper"]
        extra_kwargs = {"author": {"read_only": True}}