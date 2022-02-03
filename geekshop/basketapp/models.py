from django.db import models
from django.conf import settings
from mainapp.models import Product


class BasketManager(models.Manager):
    def count(self):
        return len(self.all())


class Basket(models.Model):
    class Meta:
        unique_together = ['user', 'product']

    objects = BasketManager()
    # objects = models.Manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}шт.'
