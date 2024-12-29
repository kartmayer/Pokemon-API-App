from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    pokedex_number = models.PositiveIntegerField(unique=True)
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField()

    def __str__(self):
        return self.name

class UserPokedex(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pokemon = models.ManyToManyField(Pokemon, related_name='pokedex')

    def __str__(self):
        return f"{self.user.username}'s Pokedex"