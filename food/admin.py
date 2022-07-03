from django.contrib import admin
from .models import *


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', ]
    sortable_by = ['-price',]
    list_filter = ['available', ]
    search_fields = ['name', ]

@admin.register(DiscountFood)
class DiscountFoodAdmin(admin.ModelAdmin):
    list_display = ['value', 'start_time', 'end_time', ]
    sortable_by = ['-time',]
    search_fields = ['value', ]