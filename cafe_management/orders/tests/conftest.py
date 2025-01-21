from orders.models import Order
from menu.models import Dish
from django.test import Client

import pytest
@pytest.fixture
def dish():
    return Dish.objects.create(name="Dish 1", price=10.00)
@pytest.fixture
def order():
    order = Order.objects.create(
        table_number=1,
        total_price=10.00,
        status='waiting'
    )
    return order

@pytest.fixture
def create_order():
    def _create_order(table_number, status):
        return Order.objects.create(table_number=table_number, status=status)
    return _create_order

@pytest.fixture
def orders():
    Order.objects.create(table_number=1, status='waiting')
    Order.objects.create(table_number=2, status='ready')
    Order.objects.create(table_number=3, status='paid')
    Order.objects.create(table_number=1, status='ready')

@pytest.fixture
def client():
    return Client()


