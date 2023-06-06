from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from decimal import Decimal
import re
from .parser.parser import parse_NB, update_price_NB, collect_data


class DollarRate(models.Model):
    '''Курс доллара'''
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.rate)

    class Meta:
        verbose_name = 'Курс доллара'
        verbose_name_plural = 'Курс доллара'


class Manufacturer(models.Model):
    '''Производитель'''
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.name, allow_unicode=True)

    def get_absolute_url(self):
        return reverse('product_list_by_manufacturer',
                       args=[self.slug])


class Category(models.Model):
    '''Категория'''
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.slug = slugify(self.name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    '''Товар'''
    GENDER_CHOICES = {
        ('M', 'Мужской'),
        ('W', 'Женский'),
        ('K', 'Детский'),
        ('ALL', 'Все')
    }
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default='ALL')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.PROTECT)
    url = models.URLField(null=True, blank=False, help_text='Ссылка на товар на другом сайте')
    image_urs = models.JSONField(null=True, blank=True)
    sizes = models.JSONField(null=True, blank=True)
    name = models.CharField(max_length=200, db_index=True, null=True, blank=True,
                            help_text='Наименование товара товара')
    slug = models.SlugField(max_length=200, db_index=True)
    dollarRate = models.ForeignKey(DollarRate, related_name='products', on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True, help_text='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Цена товара')
    color = models.CharField(max_length=200, db_index=True, null=True, blank=True, help_text='Цвет товара')
    stock = models.PositiveIntegerField(default=10, null=True, blank=True, help_text='Количество товара на складе')
    available = models.BooleanField(default=True, help_text='Товар в наличии')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'price')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ Переопередение метода сохранения для заполнения данных модели данными из сайта-донора"""
        # data = collect_data(self.url, self.manufacturer.name)
        if self.id:
            # if not Product.objects.filter(name=self.name).exists():
            if self.url:
                # Получение данных с другого сайта
                data = collect_data(self.url, self.manufacturer.name)
                price = data['price']
                images = data['images']
                sizes = data['sizes']
                sizes_json = {}
                images_json = {}
                for url in images:
                    images_json[f'image{len(images_json)}'] = url
                for size in sizes:
                    sizes_json[f'size{len(sizes_json)}'] = size
                self.sizes = sizes_json
                self.image_urs = images_json

                # Сохранение цены в поле price
                # цена = цена * курс доллара + 20% от цены
                self.price = Decimal(
                    Decimal(str(price)) * self.dollarRate.rate + Decimal(str(price / 100 * 20))).quantize(
                    Decimal('.01'))

                self.color = data['color']
                self.name = data['name']
                self.description = data['description']

                self.slug = slugify(f'{self.manufacturer.name} {self.name} {self.color}')

                # if Product.objects.filter(slug=slug).exists():
                #     slug = slugify(f'{self.manufacturer.name} {self.name} {self.color}')

            # else:
            #     # Если не удалось получить данные, вызовется исключение ValidationError
            #     raise ValidationError('Could not get data from the URL')
            else:
                # Если URL не задан, то вызовется исключение ValidationError
                raise ValidationError('URL is required')

        super(Product, self).save(*args, **kwargs)

    def update_product_price(self):
        """Обновление цены товара"""
        price = update_price_NB(self.url)
        self.price = Decimal(Decimal(str(price)) * self.dollarRate.rate + Decimal(str(price / 100 * 20))).quantize(
            Decimal('.01'))

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.category.slug, self.id, self.slug])


def create_slug(name: str) -> str:
    slug = name.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_-]+', '-', slug)
    slug = re.sub(r'^-+|-+$', '', slug)
    return slug
