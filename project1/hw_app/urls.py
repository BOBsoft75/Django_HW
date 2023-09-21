from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.get_all_products, name='products'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),
    path('orders/', views.order_view, name='orders'),
    
]