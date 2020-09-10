from django.contrib import admin

from apps.dishes.models import (
    Dish, Image, Item,
    RationDish, UserRation
)

admin.site.register(UserRation)


class ItemInline(admin.TabularInline):
    fk_name = 'ration_dish'
    model = Item


class ImagesInline(admin.TabularInline):
    fk_name = 'dish'
    model = Image


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    inlines = [ImagesInline,]


@admin.register(RationDish)
class RationDishAdmin(admin.ModelAdmin):
    inlines = [ItemInline,]
