from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)
    img = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return super.__str__(self)
