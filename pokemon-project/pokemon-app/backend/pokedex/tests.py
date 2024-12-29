from django.test import TestCase
from .models import Pokemon, User

class PokedexTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.pokemon = Pokemon.objects.create(name='Pikachu', user=self.user)

    def test_pokemon_creation(self):
        self.assertEqual(self.pokemon.name, 'Pikachu')
        self.assertEqual(self.pokemon.user.username, 'testuser')

    def test_user_pokedex(self):
        self.assertEqual(self.user.pokemon_set.count(), 1)
        self.assertEqual(self.user.pokemon_set.first().name, 'Pikachu')

    def test_pokemon_str(self):
        self.assertEqual(str(self.pokemon), 'Pikachu')