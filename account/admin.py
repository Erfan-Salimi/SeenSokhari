from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'first_name', 'last_name']
    search_fields = ['username', ]
