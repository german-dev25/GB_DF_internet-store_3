from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(
        verbose_name = 'возраст',
        blank=True,
    )
    avatar = models.ImageField(
        verbose_name = 'аватар',
        upload_to='users_avatars',
        blank=True,
    )
    phone = models.CharField(
        verbose_name = 'телефон',
        max_length= 10,
        blank=True,
    )
    cite = models.CharField(
        verbose_name='город',
        max_length=20,
        blank=True,
    )