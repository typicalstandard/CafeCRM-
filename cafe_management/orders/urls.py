from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderSearchView.as_view(), name='home'),
    path('orders/add/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/delete/', views.OrderDeleteFormView.as_view(), name='order_delete'),
    path('orders/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('total_revenue/', views.total_revenue, name='total_revenue'),


]
