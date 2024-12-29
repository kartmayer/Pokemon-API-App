from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Additional fields can be added here if needed
    pass

class Pokedex(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pokemon = models.JSONField(default=list)  # Store Pokémon data as a list of dictionaries

    def __str__(self):
        return f"{self.user.username}'s Pokedex"