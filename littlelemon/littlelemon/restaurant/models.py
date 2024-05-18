from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_quests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.no_of_quests} quests - {self.booking_date}"

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {self.price}'
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'