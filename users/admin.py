from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)  # Регистрация модели CustomUser в админ-панели Django
class CustomUserAdmin(UserAdmin):
    # Отображаемые поля в списке пользователей
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # Добавление дополнительного поля avatar к стандартным полям UserAdmin
    # Это позволит редактировать аватарку пользователя в админ-панели
    # Полная версия кода выглядит так:
    
    fieldsets = UserAdmin.fieldsets + (('Дополнительно', {'fields': ('avatar',)}),)