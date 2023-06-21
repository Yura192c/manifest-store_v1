from django.contrib import admin
from django.utils.safestring import mark_safe

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import *


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


# IMPORT EXPORT
class ProductResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, field='name')
    )
    manufacturer = fields.Field(
        column_name='manufacturer',
        attribute='manufacturer',
        widget=ForeignKeyWidget(Manufacturer, field='name')
    )
    dollarRate = fields.Field(
        column_name='dollarRate',
        attribute='dollarRate',
        widget=ForeignKeyWidget(DollarRate, field='rate')
    )

    def before_import_row(self, row, **kwargs):
        dollarRate = row["dollarRate"]
        manufacturer = row["manufacturer"]
        category = row["category"]
        DollarRate.objects.get_or_create(rate=dollarRate)
        Manufacturer.objects.get_or_create(name=manufacturer)
        Category.objects.get_or_create(name=category)

    class Meta:
        model = Product
        exclude = ('id', 'created', 'updated', 'available', 'slug', 'stock',)
        fields = (
            'gender', 'category', 'manufacturer', 'dollarRate', 'url', 'image_urs', 'sizes',
            'name', 'description', 'price', 'color',)
        export_order = (
            'name', 'description', 'color', 'manufacturer', 'dollarRate', 'price',
            'gender', 'category', 'url', 'image_urs', 'sizes',)

        import_id_fields = ('url',)


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource

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

    def get_image(self, obj):
        if obj.image_urs:
            return mark_safe(f'<img src={obj.image_urs["image1"]} width="50px" height="50px"')
        else:
            return 'Нет изображения'

    get_image.short_description = 'Изображение'
