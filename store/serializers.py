from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from store.models import Collection, Customer, OrderItem, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'unit_price', 'inventory', 'collection']



class CustomerSerializer(ModelSerializer): 
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'email', 'phone', 'membership', 'order_count']

    order_count = serializers.IntegerField()



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField()



class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'unit_price']
















# from dataclasses import field
# from decimal import Decimal
# from rest_framework import serializers
# from django.db.models import Count
# from .models import Cart, CartItem, Collection, Customer, Order, Product, Review


# class ProductSerializer(serializers.ModelSerializer):
#     collection = serializers.StringRelatedField()
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'unit_price', 'inventory', 'description', 'collection']
    
    
# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['first_name', 'last_name', 'email', 'phone']


# class CollectionSerializer(serializers.ModelSerializer):
#     products_count = serializers.IntegerField(read_only=True)
#     class Meta:
#         model = Collection
#         fields = ['id', 'title', 'products_count', 'featured_product']
        

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['customer_first_name', 'id', 'placed_at', 'payment_status']
        































































# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['product', 'name', 'description', 'date']


# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'quantity']


# class CartSerializer(serializers.ModelSerializer):
#     # items = CartItemSerializer(many=True)
#     id = serializers.UUIDField(read_only=True)
#     class Meta:
#         model = Cart
#         fields = ['id']
