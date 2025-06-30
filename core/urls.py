
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('merchant/settings/', views.merchant_settings, name='merchant_settings'),
    path('order/place/', views.place_order, name='place_order'),
    path('orders/', views.order_list, name='order_list'),
    path('simulate/', views.simulate_payment, name='simulate_payment'),
    path('register/', views.register, name='register'),


    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]



