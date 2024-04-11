from django.db import models


class CartItem(models.Model):
    user_id = models.IntegerField(null=False, blank=False)
    product_id = models.IntegerField(null=False, blank=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return self.product_id
