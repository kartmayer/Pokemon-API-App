from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pokemon, UserPokedex
from .serializers import PokemonSerializer, UserPokedexSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserPokedexViewSet(viewsets.ModelViewSet):
    queryset = UserPokedex.objects.all()
    serializer_class = UserPokedexSerializer