from django.db import models

from cart.cart_app.models.cart_model import Cart
from product.product_app.models.product_model import Product


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False)

    objects = models.Manager()

    class Meta:
        app_label = 'cart_app'

    def __str__(self):
        return f'{self.cart} | {self.product} | {self.quantity}'
