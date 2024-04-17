from django.db import models
from product.product_app.models.product_model import Product


class CartItem(models.Model):
    cart_id = models.IntegerField(null=False, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False)

    objects = models.Manager()

    class Meta:
        app_label = 'cart_app'

    def __str__(self):
        return f'{self.cart_id} | {self.product_id} | {self.quantity}'
