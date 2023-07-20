from django.db import models
from datetime import date


class Menu(models.Model):
    title = models.CharField(max_length=255, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    first_name = models.CharField(max_length=255, default=None)
    number_of_guests = models.IntegerField(default=1)
    reservation_date = models.DateField(default=date.today)
    reservation_slot = models.SmallIntegerField(default=10)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self) -> str:
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'
