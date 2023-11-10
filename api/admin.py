from django.contrib import admin

# Register your models here.
from .models import Products, Category, Order, User

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(User)
