from django.db import models

# Create your models here.

class Merchant(models.Model):
    name = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50, choices=[
        ('mobile', 'Mobile'),
        ('card', 'Card'),
        ('bank', 'Bank')
    ])
    config = models.JSONField()

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    total_amount = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
