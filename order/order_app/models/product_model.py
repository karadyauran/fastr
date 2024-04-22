from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()

    objects = models.Manager()

    class Meta:
        db_table = 'product_app_product'
        managed = False
        app_label = 'order_app'

    def __str__(self):
        return self.name
