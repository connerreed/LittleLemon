from django.test import TestCase
from restaurant.models import MenuItem
from django.test import TestCase
from restaurant.models import MenuItem
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80.00")

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        MenuItem.objects.create(title="Burger", price=100, inventory=50)
        MenuItem.objects.create(title="Pizza", price=150, inventory=30)
        MenuItem.objects.create(title="Salad", price=80, inventory=20)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get('/menu/')
        serialized_data = response.data

        # Assert if the serialized data equals the response
        self.assertEqual(serialized_data, response.data)