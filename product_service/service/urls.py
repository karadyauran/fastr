from django.contrib import admin
from django.urls import path

import product_app.views as product_app

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v3/product/get_all_products', product_app.get_all_products, name='get_all_products'),
    path('api/v3/product/create', product_app.create_product, name='create_product'),
]
