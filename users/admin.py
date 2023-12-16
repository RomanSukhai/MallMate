from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import City, Mall, Shop

# Реєстрація моделей для адмін-панелі
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Mall)
class MallAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['cities']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'mall', 'x', 'y']
    list_filter = ['mall']
    search_fields = ['name', 'mall__name']
