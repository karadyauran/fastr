from django.contrib import admin
from django.urls import path

import order.order_app.views.order_view as order_view
import order.order_app.views.order_item_view as order_item_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/order/get', order_view.get, name='order_get'),

    path('api/v1/order_item_view/add_all_from_cart', order_item_view.add_all_from_cart, name='add_all_from_cart'),
]
