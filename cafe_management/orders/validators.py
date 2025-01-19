from django.core.exceptions import ValidationError
from .models import Order

def validate_order_id(order_id):
    if not Order.objects.filter(id=order_id).exists():
        raise ValidationError('Заказ с указанным ID не найден.')
    return order_id
