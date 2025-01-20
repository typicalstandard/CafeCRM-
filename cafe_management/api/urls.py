from django.urls import path
from .views import CreateOrderAPIView, DeleteOrderAPIView, SearchOrderAPIView

urlpatterns = [
    path('orders/create/', CreateOrderAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/delete/', DeleteOrderAPIView.as_view(), name='order-delete'),
    path('orders/search/', SearchOrderAPIView.as_view(), name='order-search'),
]
