"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import cart_item.views as cart_view
import order.views as order_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v3/add', cart_view.add, name='add'),
    path('api/v3/cart', cart_view.get, name='get'),
    path('api/v3/remove', cart_view.remove, name='remove'),

    path('api/v3/list_orders', order_view.order_list, name='order_list'),
    path('api/v3/add_order', order_view.order_add, name='order_add'),
    path('api/v3/delete_order', order_view.order_delete, name='order_delete'),
    path('api/v3/update_order', order_view.order_update, name='order_update'),

    path('api/v3/get_order_item', order_view.get_order_item, name='get_order_item'),
    path('api/v3/order_item_create', order_view.order_item_create, name='order_item_create'),
    path('api/v3/order_item_delete', order_view.order_item_delete, name='order_item_delete'),
]
