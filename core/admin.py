
# Register your models here.

from django.contrib import admin
from .models import Merchant, Order

admin.site.register(Merchant)
admin.site.register(Order)
