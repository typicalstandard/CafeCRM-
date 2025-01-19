from rest_framework import viewsets
from .serializers import OrderSerializer
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
