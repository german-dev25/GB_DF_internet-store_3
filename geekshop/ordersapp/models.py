from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from basketapp.models import Basket
from mainapp.models import Product


class Order(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created',)

    CREATED = 'CREATED'
    IN_PROCESSING = 'IN_PROCESSING'
    AWAITING_PAYMENT = 'AWAITING_PAYMENT'
    PAID = 'PAID'
    READY = 'READY'
    CANCELED = 'CANCELED'
    FINISHED = 'FINISHED'

    ORDER_STATUS_CHOICES = (
        (CREATED, 'Создан'),
        (IN_PROCESSING, 'В обработке'),
        (AWAITING_PAYMENT, 'Ожидает оплаты'),
        (PAID, 'Оплачен'),
        (READY, 'Готов к выдаче'),
        (CANCELED, 'Отменен'),
        (FINISHED, 'Выдан'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус', choices=ORDER_STATUS_CHOICES, max_length=16, default=CREATED)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def __str__(self):
        return f'Заказ {self.id}'

    @property
    def items_with_products(self):
        return self.items.select_related('product')

    def get_total_cost(self):
        return sum(item.cost for item in self.items_with_products)

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    objects = models.Manager()
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    @property
    def cost(self):
        return self.product.price * self.quantity


@receiver(pre_save, sender=OrderItem)
def product_quantity_update_on_order_item_save(
        sender, update_fields, instance, **kwargs
):
    if instance.pk:
        old_item = OrderItem.objects.get(pk=instance.pk)
        instance.product.quantity -= instance.quantity - old_item.quantyti
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()


@receiver(pre_delete, sender=OrderItem)
def product_quantity_update_on_order_item_delete(
        sender, instance, **kwargs
):
    instance.product.quantity += instance.quantity()
    instance.product.save()
