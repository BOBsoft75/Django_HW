from django.contrib import admin
from . import models
# from hw_app.models import Category

# admin.site.register(Category)
# admin.site.register(Product)


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(amount=0)


# admin.site.register(Author) используем декоратор для каждой медели класса
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    ordering = ['-amount']
    list_filter = ['added_at']  # добавляет фильтр
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    # fields = ['name', 'description', 'price', 'amount', 'image', 'added_at']
    readonly_fields = ['added_at']
    fieldsets = [
        (
            None, {  # используем поле без определенного названия
                # класс ['wide'] максимально большое поле в панели
                'classes': ['wide'],
                'fields': ['name'],  # в качестве поля name
            },
        ),
        (
            'Подробности',  # блок подробности
            {
                'classes': ['collapse'],  # схлопнутое поле(скрытое)
                # при развороте выдает описание
                'description': 'Категория товара и его подробное описание',
                # те поля которые мы спрятали
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Дата добавления',
            {
                'description': 'Дата внесения товара в базу',
                'fields': ['added_at'],
            }
        ),
    ]


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (name)'

    readonly_fields = ['reg_date']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'common_price']

    readonly_fields = ['date']
