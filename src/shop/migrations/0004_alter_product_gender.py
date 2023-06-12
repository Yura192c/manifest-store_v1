# Generated by Django 4.2.1 on 2023-06-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_available_alter_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('K', 'Детский'), ('W', 'Женский'), ('ALL', 'Все'), ('M', 'Мужской')], default='ALL', max_length=3),
        ),
    ]