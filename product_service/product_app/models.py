from django.db import models
from django.db.models import CharField


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="No description")
    category = models.CharField(max_length=100, default="No category")

    def __str__(self) -> CharField:
        return self.name
