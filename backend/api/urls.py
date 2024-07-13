from django.urls import path
from . import views

urlpatterns = [
    path("animals/", views.AnimalListCreate.as_view(), name="animal-list"),
    path("animals/delete/<int:pk>/", views.AnimalDelete.as_view(), name="delete-animal")
]
 