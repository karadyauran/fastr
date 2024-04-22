from django.db import models

from order.order_app.models.cart_model import Cart
from order.order_app.models.product_model import Product


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False)

    objects = models.Manager()

    class Meta:
        db_table = 'cart_app_cartitem'
        managed = False
        app_label = 'order_app'

    def __str__(self):
        return f'{self.cart} | {self.product} | {self.quantity}'
