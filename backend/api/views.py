from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, AnimalSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Animal

#View for creating a new animal
class AnimalListCreate(generics.ListCreateAPIView):
    #Set the serializer_class to AnimalSerializer and only grant authenticated users permission to access this view
    serializer_class = AnimalSerializer
    permission_class = [IsAuthenticated]
    
    #Function for returning all animals
    #def get_all_animals():
        #return Animal.objects.all()
    
    #Function for returning animals created by the user
    def get_queryset(self):
        user = self.request.user
        return Animal.objects.filter(zookeeper=user)
    
    #Function for creating animals
    def perform_create(self, serializer):
        #If the serializer is valid, save the animal and set zookeeper as the user
        if serializer.is_Valid():
            serializer.save(zookeeper=self.request.user)
        else:
            #Otherwise, print errors
            print(serializer.errors)

class AnimalDelete(generics.DestroyAPIView):
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Animal.objects.filter(zookeeper=user)
    
        
    
    
#View for creating a new user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
