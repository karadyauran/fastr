from django.contrib import admin
from django.urls import path

import product.product_app.views.views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/products', product_views.product_list, name='product_list'),
    path('api/v1/create_product', product_views.product_create, name='product_create'),
]
