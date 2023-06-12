from django.db import models
from src.shop.models import Product


class Order(models.Model):
    first_name = models.CharField('Имя',max_length=50)
    last_name = models.CharField('Фамилия',max_length=50)
    email = models.EmailField('Почта')
    address = models.CharField('Адрес доставки',max_length=250)
    postal_code = models.CharField('Почтовый индекс',max_length=20)
    city = models.CharField('Город',max_length=100)
    country = models.CharField('Страна',max_length=100)
    created = models.DateTimeField('Обновлен',auto_now_add=True)
    updated = models.DateTimeField('Создан',auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    size = models.CharField(max_length=10, default='-')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
