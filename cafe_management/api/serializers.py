# orders/serializers.py
from rest_framework import serializers
from menu.models import Dish
from orders.models import Order

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Dish.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'items', 'total_price', 'status']
        read_only_fields = ['total_price', 'status']

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        order.items.set(items)
        return order
