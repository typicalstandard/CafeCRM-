from django.urls import path
from .views import CreateOrderAPIView

urlpatterns = [
    path('orders/create/', CreateOrderAPIView.as_view(), name='order-create'),
]
