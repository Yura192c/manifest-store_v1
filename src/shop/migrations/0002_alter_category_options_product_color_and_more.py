# Generated by Django 4.2.1 on 2023-06-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('K', 'Детский'), ('W', 'Женский'), ('ALL', 'Все'), ('M', 'Мужской')], default='ALL', max_length=3),
        ),
    ]
