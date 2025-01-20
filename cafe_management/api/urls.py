from django.urls import path
from .views import CreateOrderAPIView, DeleteOrderAPIView, SearchOrderAPIView, OrderUpdateStatusAPIView

urlpatterns = [
    path('orders/create/', CreateOrderAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/delete/', DeleteOrderAPIView.as_view(), name='order-delete'),
    path('orders/search/', SearchOrderAPIView.as_view(), name='order-search'),
    path('orders/<int:pk>/update_status/', OrderUpdateStatusAPIView.as_view(), name='order-update-status'),
]
