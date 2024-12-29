from rest_framework import serializers
from .models import Pokemon, UserPokedex

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

class UserPokedexSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPokedex
        fields = ['user', 'pokemon']