from django.test import TestCase
from django.urls import reverse
from restaurant.models import Booking, Menu
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class MenuViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        Menu.objects.create(title="Test Menu Item", price=10.00, inventory=100)

    def test_get_all(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
