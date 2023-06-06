from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'dollarRate', 'price',
                    'available', 'updated', 'category', 'manufacturer', 'gender', 'color', 'get_image', 'id', 'slug']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'gender']
    search_fields = ('name', 'manufacturer__name', 'category__name')
    radio_fields = {"dollarRate": admin.VERTICAL,
                    "manufacturer": admin.HORIZONTAL}
    fieldsets = (
        ('Автоматическое добавление', {
            'fields': ('gender', 'category', 'manufacturer', 'url', 'dollarRate')
        }),
        ('Ручное добавление', {
            'classes': ['collapse'],
            'fields': ('name', 'description', 'price', 'available', 'image_urs', 'sizes', 'slug', 'color')
        })
    )
    # actions = ['update_price', 'publish', 'unpublish']
    # actions = ['publish', 'unpublish']

    def get_image(self, obj):
        # return mark_safe(f'<img src="{obj.image_urs.image1}" width="100px" />'.format(obj.image_urs[0]))
        return mark_safe(f'<img src={obj.image_urs["image1"]} width="50px" height="50px"')

    get_image.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(DollarRate)
class DollarRateAdmin(admin.ModelAdmin):
    list_display = ['rate']


admin.site.site_title = 'Manifest Store Admin'
admin.site.site_header = 'Manifest Store Admin'
