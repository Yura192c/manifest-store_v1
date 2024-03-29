# Generated by Django 4.2.1 on 2023-06-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_options_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, help_text='Товар в наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, db_index=True, help_text='Цвет товара', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Описание товара', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('W', 'Женский'), ('ALL', 'Все'), ('K', 'Детский'), ('M', 'Мужской')], default='ALL', max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, db_index=True, help_text='Наименование товара товара', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Цена товара', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(blank=True, default=10, help_text='Количество товара на складе', null=True),
        ),
    ]
