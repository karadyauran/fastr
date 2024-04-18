from django.db import models

from authentication.authenticate_app.models import UserAuth


class Cart(models.Model):
    user = models.ForeignKey(UserAuth, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    objects = models.Manager()

    class Meta:
        app_label = 'cart_app'

    def set_total_price(self, total):
        self.total = total

    def __str__(self):
        return f'{self.user} | {self.total}'
