from django.db import models
from menu.models import Dish


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    table_number = models.IntegerField()
    items = models.ManyToManyField(Dish)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=[
        ('waiting', 'в ожидании'),
        ('ready', 'готово'),
        ('paid', 'оплачено')
    ], default='waiting')

