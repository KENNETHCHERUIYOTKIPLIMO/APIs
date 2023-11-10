# Create your views here.
from django.shortcuts import render
from .models import Products, User, Order, Category
from .serializer import ProductSerializer, UserSerializer, OrderSerializer, CategorySerializer
from rest_framework import viewsets


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderView(viewsets.ModelViewSet):
        queryset = Order.objects.all()
        serializer_class = OrderSerializer


class UserView(viewsets.ModelViewSet):
            queryset =User.objects.all()
            serializer_class = UserSerializer