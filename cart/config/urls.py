from django.contrib import admin
from django.urls import path

import cart.cart_app.views as cart_app

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/cart/get_cart', cart_app.get, name='get_cart'),

    path('api/v1/cart/add_item_to_cart', cart_app.add, name='add_item_to_cart'),
    path('api/v1/cart/edit_cart_item_quantity', cart_app.edit_cart_item_quantity, name='edit_cart_item_quantity'),
    path('api/v1/cart/remove', cart_app.remove, name='remove'),

    path('api/v1/cart/create_cart', cart_app.create_cart, name='create_cart'),
]
