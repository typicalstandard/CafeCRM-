import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cafe_management.settings')
django.setup()

from orders.models import  Order
from menu.models import Dish

dish1 = Dish.objects.create(name='Dish 1', price=10.50)
dish2 = Dish.objects.create(name='Dish 2', price=12.75)
dish3 = Dish.objects.create(name='Dish 3', price=8.20)
dish4 = Dish.objects.create(name='Dish 4', price=15.00)
dish5 = Dish.objects.create(name='Dish 5', price=11.30)

order1 = Order.objects.create(table_number=1, status='ready')
order1.items.add(dish1, dish2)

order2 = Order.objects.create(table_number=2, status='waiting')
order2.items.add(dish3, dish4)

order3 = Order.objects.create(table_number=3, status='paid')
order3.items.add(dish5)

order4 = Order.objects.create(table_number=4, status='ready')
order4.items.add(dish1, dish3)

order5 = Order.objects.create(table_number=5, status='waiting')
order5.items.add(dish2, dish4)

order6 = Order.objects.create(table_number=6, status='paid')
order6.items.add(dish5)
