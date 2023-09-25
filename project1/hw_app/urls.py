from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.get_all_products, name='products'),
    path('change_product/<int:product_id>/',
         views.change_product, name='change_product'),  # если пользователь введет client а после <int:client_id> то сработает представление client_order которое вернет заказы
    path('orders/', views.order_view, name='orders'),
    path('clients/', views.clients_view, name='clients'),
    #     path('__debug__/', include("debug_toolbar.urls")),
    path('change_clients/<int:client_id>/',
         views.change_client, name='change_client'),

]
