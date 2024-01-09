from django.test import TestCase
from restaurant.models import Booking, Menu


class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title="Test Menu Item", price=10.00, inventory=100)

    def test_menu_item(self):
        menu_item = Menu.objects.get(title="Test Menu Item")
        self.assertEqual(menu_item.title, "Test Menu Item")
        self.assertEqual(menu_item.price, 10.00)
        self.assertEqual(menu_item.inventory, 100)