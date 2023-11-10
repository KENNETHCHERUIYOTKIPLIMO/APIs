from rest_framework import serializers

from .models import Products, Category, Order, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
            class Meta:
                model = Category
                fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
          class Meta:
           model = Order
           fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
          class Meta:
            model = User
            fields = '__all__'


