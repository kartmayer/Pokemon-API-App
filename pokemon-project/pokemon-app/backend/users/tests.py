from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_pokedex_relationship(self):
        # Assuming a Pokedex model exists with a ForeignKey to User
        from pokedex.models import Pokedex
        pokedex = Pokedex.objects.create(user=self.user)
        self.assertEqual(pokedex.user, self.user)