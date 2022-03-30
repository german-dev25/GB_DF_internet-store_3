from django.db import models


class ProductCategory(models.Model):
    objects = models.Manager()
    name = models.CharField(
        verbose_name='имя',
        max_length=100
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=100,
    )
    price = models.DecimalField(
        verbose_name='цена',
        decimal_places=2,
        max_digits=7,
    )
    color = models.PositiveIntegerField(
        verbose_name='цвет',
        default=0x000000,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    image = models.ImageField(
        verbose_name='картинка',
        blank=True,
        upload_to='products',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    def __str__(self):
        return self.name
