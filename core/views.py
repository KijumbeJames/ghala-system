
# Create your views here.
import threading
import time
from django.shortcuts import render, redirect
from .models import Merchant, Order
from .forms import MerchantForm, OrderForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def merchant_settings(request):
    if request.method == 'POST':
        form = MerchantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('merchant_settings')
    else:
        form = MerchantForm()
    return render(request, 'core/merchant_settings.html', {'form': form})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            threading.Thread(target=simulate_payment, args=(order.id,)).start()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'core/place_order.html', {'form': form})

def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'core/orders.html', {'orders': orders})

def simulate_payment(order_id):
    time.sleep(5)
    order = Order.objects.get(id=order_id)
    order.status = 'paid'
    order.save()

def home(request):
    return render(request, 'home.html')

def simulate_payment_thread():
    time.sleep(5)
    pending_orders = Order.objects.filter(status='pending')
    for order in pending_orders:
        order.status = 'paid'
        order.save()

def simulate_payment(request):
    threading.Thread(target=simulate_payment_thread).start()
    return redirect('order_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log them in immediately
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
