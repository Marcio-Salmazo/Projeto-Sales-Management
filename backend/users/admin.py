from django.contrib import admin
from .models import Customers, Employee

# Register your models here.
admin.site.register(Customers)
admin.site.register(Employee)