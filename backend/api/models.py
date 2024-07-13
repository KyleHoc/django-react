from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Animal(models.Model):
    species = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    favorite_food = models.CharField(max_length=30)
    added_to_zoo = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    photo = models.ImageField(upload_to='images/')
    zookeeper = models.ForeignKey(User, on_delete=models.CASCADE, related_name="animals")
    
def __str__(self):
    return self.name