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

class ReviewSerializer(ModelSerializer):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.Charfield(max_length=255)
    description = models.TextFiled()
    date = models.DateTimeField(auto_now_add=True)




































































