from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # <-- This is the new home page route
    path('merchant/settings/', views.merchant_settings, name='merchant_settings'),
    path('order/place/', views.place_order, name='place_order'),
    path('orders/', views.order_list, name='order_list'),
]

