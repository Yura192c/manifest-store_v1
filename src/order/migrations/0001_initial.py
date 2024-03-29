# Generated by Django 4.2.1 on 2023-06-12 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0004_alter_product_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес доставки')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Почтовый индекс')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Создан')),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.product')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['-created'], name='order_order_created_708daa_idx'),
        ),
    ]
