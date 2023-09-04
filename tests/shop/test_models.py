from django.test import TestCase
from src.shop.models import *

class TestCategory(TestCase):
    def setUp(self):
        Category.objects.create(name='test_category', slug='test_category')

    def test_category(self):
        category = Category.objects.get(name='test_category')
        self.assertEqual(category.name, 'test_category')
        self.assertEqual(category.slug, 'test_category')

    def test_category_str(self):
        category = Category.objects.get(name='test_category')
        self.assertEqual(str(category), 'test_category')


class TestProduct(TestCase):
    def setUp(self):
        category = Category.objects.create(name='test_category', slug='test_category')
        dollar_rate = DollarRate.objects.create(rate=1)
        manufacturer = Manufacturer.objects.create(name='test_manufacturer', slug='test_manufacturer')
        Product.objects.create(category=category,
                               name='test_product',
                               slug='test_product',
                               dollarRate=dollar_rate,
                                 manufacturer=manufacturer,
                               price=1000)

    def test_product(self):
        product = Product.objects.get(name='test_product')
        self.assertEqual(product.name, 'test_product')
        self.assertEqual(product.slug, 'test_product')
        self.assertEqual(product.price, 1000)

    def test_product_str(self):
        product = Product.objects.get(name='test_product')
        self.assertEqual(str(product), 'test_product')
