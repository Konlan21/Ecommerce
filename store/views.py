from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet

from store.serializers import OrderItemSerializer
from . models import OrderItem, Product




class OrderItemList(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productser























# from django.db.models.aggregates import Count
# from rest_framework.response import Response
# from rest_framework.generics import *
# from . serializers import CollectionSerializer, CustomerSerializer
# from .models import Customer, Collection


# class CustomerViewSet(ListAPIView):
#     queryset = Customer.objects.prefetch_related('order').annotate(order_count=Count('order')).all()
#     serializer_class = CustomerSerializer

# class CustomerDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.annotate(order_count=Count('order')).all()
#     serializer_class = CustomerSerializer



# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.annotate(products_count=Count('product')).all() 
#     serializer_class = CollectionSerializer


# class CollectionDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.annotate(products_count=Count('product')).all()  
#     serializer_class = CollectionSerializer 
#     lookup_field = 'title'





# from django.shortcuts import get_object_or_404
# from rest_framework.status import HTTP_204_NO_CONTENT
# from rest_framework.decorators import api_view
# from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView
# from rest_framework.response import Response
# from .models import Cart, Collection, Customer, Product
# from .serializers import CartSerializer, CollectionSerializer, CustomerSerializer, ProductSerializer



# class CustomerList(CreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
    

# class CartView(CreateAPIView, RetrieveDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     lookup_field = ['pk']

#     # def destroy(self, request):
#     #     cart = get_object_or_404(Cart)
#     #     cart.delete()
#     #     return Response(status=HTTP_204_NO_CONTENT)




# # class OrderList(APIView):
# #     def get(self, request):
# #         products = Product.objects.order_by('-unit_price').all()
# #         serializer = ProductSerializer(products, many=True)
# #         return Response(serializer.data)
# #     def post(self, request):
# #         serializer = ProductSerializer(data=request.dat)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)
        
# # @api_view(['GET', 'POST'])
# # def customers_api(request):
# #     if request.method == 'GET':
# #         customers = Customer.objects.all()
# #         serializer = CustomerSerializer(customers, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = CustomerSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def customer_detail(request, email):
# #     customer = get_object_or_404(Customer, email=email)
# #     if request.method == 'GET':
# #         serializer = CustomerSerializer(customer)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT':
# #         serializer = CustomerSerializer(customer, data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)
# #     elif request.method == 'DELETE':
# #         customer.delete()
# #         return Response(status=HTTP_204_NO_CONTENT)







# # # @api_view()
# # # def product_list(request):
# # #     products = Product.objects.all()
# # #     serializer = ProductSerializer(products, many=True)
# # #     return Response(serializer.data)

# # # @api_view()
# # # def product_detail(request, id):
# # #     product = get_object_or_404(Product, id=id)
# # #     serializer = ProductSerializer(product)
# # #     return Response(serializer.data)
    

# # # @api_view(['GET', 'POST'])
# # # def collection_list(request):
# #     if request.method == 'GET':    
# #         collection = Collection.objects.all()
# #         serializer = CollectionSerializer(collection, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = CollectionSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)


# # @api_view(['GET', 'PUT', 'DELETE'])
# # def collection_detail(request, title):
# #     collection = get_object_or_404(Collection, title=title)
# #     if request.method == 'GET':
# #         serializer = CollectionSerializer(collection)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT':
# #         serializer = CollectionSerializer(collection, data=request.data)
# #         serializer.is_valid()
# #         serializer.save()
# #         return Response(serializer.data)
# #     elif request.method == 'DELETE':
# #         collection.delete()
# #         return Response(status=HTTP_204_NO_CONTENT)
    
        






# # from rest_framework.viewsets import ModelViewSet
# # from rest_framework.filters import SearchFilter
# # from django_filters.rest_framework import DjangoFilterBackend
# # from .models import Collection, Customer, Order, Product, Review
# # from .serializers import CollectionSerializer, CustomerSerializer, OrderSerializer, ProductSerializer, ReviewSerializer


# # class ProductViewSet(ModelViewSet):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
# #     filter_backends = [DjangoFilterBackend, SearchFilter]
# #     filterset_fields = ['collection_id']
# #     search_fields = ['title', 'description']

# # class CollectionViewSet(ModelViewSet):
# #     queryset = Collection.objects.all()
# #     serializer_class = CollectionSerializer

# # class CustomerViewSet(ModelViewSet):
# #     queryset = Customer.objects.all()
# #     serializer_class = CustomerSerializer
# #     filter_backends = [DjangoFilterBackend]
# #     filterset_fields = ['order']


# # class ReviewViewSet(ModelViewSet):
# #     queryset = Review.objects.all()
# #     serializer_class = ReviewSerializer

# # class OrderViewSet(ModelViewSet):
# #     queryset = Order.objects.all()
# #     serializer_class = OrderSerializer
# #     filter_backends = [DjangoFilterBackend, SearchFilter]
# #     filterset_fields = ['customer']
# #     search_fields = ['id']





# # class ProductList(ListCreateAPIView):
# #     queryset = Product.objects.select_related('collection').all()
# #     serializer_class = ProductSerializer



# # class CollectionList(ListCreateAPIView):
# #     queryset = Collection.objects.annotate(products_count=Count('product')).all()
# #     serializer_class = CollectionSerializer


# # class ProductList(APIView):
# #     def get(self, request):
# #         products = Product.objects.select_related('collection').all()
# #         serializer = ProductSerializer(products, many=True)
# #         return Response(serializer.data)
# #     def post(self, request):
# #         serializer = ProductSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         return Response(serializer.data, status=HTTP_201_CREATED)


# # class ProductDetail(APIView):
# #     def get(self, request, id):
# #         product_detail = get_object_or_404(Product, pk=id)
# #         serializer = ProductSerializer(product_detail)
# #         return Response(serializer.data)
    
# #     def put(self, request, id):
# #         product_detail = get_object_or_404(Product, pk=id)
# #         serializer = ProductSerializer(product_detail, data=request.data)
# #         serializer.is_valid()
# #         serializer.save()

# #     def delete(self, request, id):
# #         product_detail = get_object_or_404(Product, pk=id)
# #         product_detail.delete()
# #         return Response(status=HTTP_204_NO_CONTENT)









# # @api_view(['GET', 'POST'])
# # def product_list(request):
# #     if request.method == 'GET':
# #         products = Product.objects.select_related('collection').all()
# #         serializer = ProductSerializer(products, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = ProductSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         return Response(serializer.data, status=HTTP_201_CREATED)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def product_detail(request, id):
# #     product_detail = get_object_or_404(Product, pk=id)
# #     if request.method == 'GET':
# #         serializer = ProductSerializer(product_detail)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT':
# #         serializer = ProductSerializer(product_detail, data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)
# #     elif request.method == 'DELETE':
# #         product_detail.delete()
# #         return Response(status=HTTP_204_NO_CONTENT)



# # @api_view(['GET', 'POST'])
# # def customers(request):
# #     if request.method == 'GET':
# #         customers = Customer.objects.filter(payment_status='C').all()
# #         serializer = CustomerSerializer(customers, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = CustomerSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=HTTP_201_CREATED)


# # @api_view(['GET', 'PUT'])
# # def customer_detail(request, email):
# #     customer = get_object_or_404(Customer, email=email)
# #     if request.method == 'GET':
# #         serializer = CustomerSerializer(customer)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT':
# #         serializer = CustomerSerializer(customer, data=request.data)
# #         serializer.is_valid()
# #         serializer.save()
# #         return Response(serializer.data)

# # @api_view(['GET', 'POST'])
# # def collection_list(request):
# #     if request.method == 'GET':    
# #         collections_list = Collection.objects.all()
# #         serializer = CollectionSerializer(collections_list, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = CollectionSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=HTTP_201_CREATED)

# # @api_view(['GET', 'PUT', 'DELETE'])
# # def collection_detail(request, title):
# #     collection = get_object_or_404(Collection, title=title)
# #     if request.method == 'GET': 
# #         serializer = CollectionSerializer(collection)
# #         return Response(serializer.data)
# #     elif request.method == 'PUT':
# #         serializer = CollectionSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=HTTP_201_CREATED)
# #     elif request.method == 'DELETE':
# #         collection.delete()




























































































# #         return Response(status=HTTP_204_NO_CONTENT)

# # @api_view(['GET', 'POST'])
# # def orders_api(request):
# #     if request.method == 'GET':
# #         orders = Order.objects.all()
# #         serializer = OrderSerializer(orders, many=True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = OrderSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=HTTP_201_CREATED)


# # @api_view()
# # def order_detail(request, payment_status):
# #     order = get_object_or_404(Order, payment_status=payment_status)
# #     serializer = OrderSerializer(order)
# #     return Response(serializer.data)