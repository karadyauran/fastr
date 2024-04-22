from django.db import models

from payment.payment_app.models import UserAuth


class Order(models.Model):
    user = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, default='PENDING')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    objects = models.Manager()

    class Meta:
        db_table = 'order_app_order'
        managed = False
        app_label = 'order_app'

    def set_total_price(self, total):
        self.total = total

    def __str__(self):
        return f'{self.user} | {self.total}'
