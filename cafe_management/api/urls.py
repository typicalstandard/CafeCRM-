from django.urls import path
from .views import CreateOrderAPIView, DeleteOrderAPIView

urlpatterns = [
    path('orders/create/', CreateOrderAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/delete/', DeleteOrderAPIView.as_view(), name='order-delete'),
]
