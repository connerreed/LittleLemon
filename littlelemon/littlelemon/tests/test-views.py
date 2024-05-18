from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pancake", price=12, inventory=22)
        Menu.objects.create(title="Soup", price=21, inventory=16)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        self.assertEqual(MenuSerializer(items, many=True).data, serialized_items.data)