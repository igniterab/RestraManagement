from django.contrib import admin
from .models import MenuItem, FoodCategory, Ingridients, Orders

class FoodCategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name',
    'category', 
    'description',
    'available',
    'price',
    'is_veg',
    'quantity')

    list_filter = ['category', 'is_veg', 'available']

class IngridientsAdmin(admin.ModelAdmin):
    list_display = ('name',
    'available',
    'quantity')

    list_filter = ['available']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('customer_name',
    'mobile',
    'table_num',
    'is_accepted',
    'total',
    'payment_method',
    'is_cancelled_by_user',
    'delievery_boy',
    'prep_time',)


admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Ingridients, IngridientsAdmin)
admin.site.register(Orders, OrdersAdmin)