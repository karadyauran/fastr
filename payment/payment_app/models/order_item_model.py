from django.db import models

from payment.payment_app.models import Order
from payment.payment_app.models import Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False)

    objects = models.Manager()

    class Meta:
        db_table = "order_app_orderitem"
        managed = False
        app_label = 'order_app'

    def __str__(self):
        return f'{self.order} | {self.product} | {self.quantity}'
