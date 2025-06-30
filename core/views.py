
# Create your views here.
import threading
import time
from django.shortcuts import render, redirect
from .models import Merchant, Order
from .forms import MerchantForm, OrderForm

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
    return render(request, 'core/home.html')
