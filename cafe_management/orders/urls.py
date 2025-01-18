from django.urls import path
from . import views

urlpatterns = [
    path('orders/add/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/delete/', views.OrderDeleteFormView.as_view(), name='order_delete'),
    path('orders/search/',views.OrderSearchView.as_view(),name='order_search'),
]
