from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    password = models.CharField(max_length=130)
    date_joined = models.DateTimeField(auto_now_add=True)

    profile_image = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return f'{self.email} : {self.first_name} {self.last_name}'
