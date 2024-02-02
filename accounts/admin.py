from django.contrib import admin
from .models import UserAccount
from django.contrib.admin import ModelAdmin


@admin.register(UserAccount)
class CustomUserAdmin(ModelAdmin):
    model = UserAccount
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin']

