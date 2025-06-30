from django import forms
from .models import Merchant, Order

class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ['name', 'payment_method', 'config']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['merchant', 'product_name', 'total_amount']
