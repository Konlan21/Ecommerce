from django.urls import path
from . import views


urlpatterns = [
    path('order_items/', views.OrderItemList.as_view()),
    path('order_items/<int:pk>/', views.OrderItemDetail.as_view())
]
























































































# from django.urls import path
# from . import views


# urlpatterns = [
#     # path('products_list/', views.ProductList),
#     # path('products/<str:id>/', views.product_detail),
#     # path('collection_list/', views.collection_list),
#     # path('collection_list/<str:title>/', views.collection_detail)
#     # path('orders/', views.OrderList.as_view()),
#     path('customers_api/', views.CustomerList.as_view()),
#     # path('customers_api/<str:email>/', views.customer_detail)
#     path('cart/', views.CartView.as_view()),
#     path('cart/<int:pk>/', views.CartView.as_view())
# ]







# # # from django.urls import path
# # from cgitb import lookup
# # from rest_framework.routers import DefaultRouter
# # from rest_framework_nested import routers
# # from . import views

# # router = DefaultRouter()
# # router.register('products', views.ProductViewSet)
# # router.register('collections', views.CollectionViewSet)
# # router.register('customers', views.CustomerViewSet)
# # router.register('reviews', views.ReviewViewSet)
# # router.register('orders', views.OrderViewSet)
# # products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
# # products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# # urlpatterns = router.urls + products_router.urls




# # # urlpatterns = [
# # #     path('products/', views.ProductList.as_view()),
# # #     path('products/<int:id>/', views.ProductDetail.as_view()),
# # #     path('customers/', views.customers),
# # #     path('customers/<str:email>/', views.customer_detail),
# # #     path('collections/', views.CollectionList.as_view()),
# # #     path('collections/<str:title>/', views.collection_detail),
# # #     path('orders_list/', views.orders_api),
# # #     path('orders_list/<str:payment_status>/', views.order_detail)
# # # ]
