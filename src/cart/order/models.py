from django.db import models
from django.db.models import ForeignKey


class Order(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    product_id = models.IntegerField(null=False, blank=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} {self.product_id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.IntegerField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> ForeignKey:
        return self.order
