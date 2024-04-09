from django.db import models
from django.db.models import CharField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> CharField:
        return self.name
