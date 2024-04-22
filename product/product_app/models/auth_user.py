from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class UserAuth(AbstractBaseUser):
    last_login = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=120, null=False)
    last_name = models.CharField(max_length=120, null=False)
    password = models.CharField(max_length=125)
    location = models.CharField(max_length=100, null=True)
    profile_photo = models.CharField(max_length=250, null=True)
    create_date = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']

    objects = models.Manager()

    class Meta:
        db_table = 'authenticate_app_userauth'
        managed = False
        app_label = 'product_app'

    def __str__(self) -> str:
        return f'{self.username} {self.email}'
