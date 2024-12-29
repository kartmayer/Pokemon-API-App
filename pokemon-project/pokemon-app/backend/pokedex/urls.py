from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, UserPokedexViewSet

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet)
router.register(r'userpokedex', UserPokedexViewSet)

urlpatterns = [
    path('', include(router.urls)),
]