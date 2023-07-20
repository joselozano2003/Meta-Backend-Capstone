from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="IceCream", price=Decimal('80'), inventory=50)
        self.assertEqual(str(item), "IceCream : 50")

    def test_default_inventory(self):
        item = Menu.objects.create(title="Cake", price=Decimal('20'))
        self.assertEqual(item.inventory, 20)
