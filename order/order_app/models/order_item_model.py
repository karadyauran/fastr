from django.db import models

from order.order_app.models.order_model import Order
from product.product_app.models.product_model import Product


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False)

    objects = models.Manager()

    class Meta:
        app_label = 'cart_app'

    def __str__(self):
        return f'{self.order} | {self.product} | {self.quantity}'
