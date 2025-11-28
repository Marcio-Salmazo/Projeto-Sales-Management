from django.contrib import admin
from .models import Product_Sale, Sale, PaymentMethod

# Register your models here.
admin.site.register(Product_Sale)
admin.site.register(Sale)
admin.site.register(PaymentMethod)
