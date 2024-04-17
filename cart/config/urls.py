from django.contrib import admin
from django.urls import path

import cart.cart_app.views as cart_app

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/get_cart', cart_app.get, name='get_cart'),

    path('api/v1/add_item_to_cart', cart_app.add, name='add_item_to_cart'),
    path('api/v1/edit_cart_item_quantity', cart_app.edit_cart_item_quantity, name='edit_cart_item_quantity'),
    path('api/v1/remove', cart_app.remove, name='remove'),
]
