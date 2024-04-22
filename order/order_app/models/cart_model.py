from django.db import models

from order.order_app.models.auth_user import UserAuth


class Cart(models.Model):
    user = models.ForeignKey(UserAuth, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    objects = models.Manager()

    class Meta:
        db_table = 'cart_app_cart'
        managed = False
        app_label = 'order_app'

    def set_total_price(self, total):
        self.total = total

    def __str__(self):
        return f'{self.user} | {self.total}'
