from django.shortcuts import render
from django.views import View

# Добавьте в начало файла после существующего MENU
CABINET_MENU = [
    {'title': 'Все заявки', 'url': '/cabinet/visits/', 'icon': 'bi-list-ul', 'active': False},
    {'title': 'Новые заявки', 'url': '/cabinet/visits/new/', 'icon': 'bi-bell', 'active': False},
    {'title': 'Архив заявок', 'url': '/cabinet/visits/archive/', 'icon': 'bi-archive', 'active': False},
    {'title': 'Сменить пароль', 'url': '/cabinet/password/', 'icon': 'bi-key', 'active': False},
]

def get_cabinet_menu_context(current_url: str) -> dict:
    menu = CABINET_MENU.copy()
    for item in menu:
        if item['url'] == current_url:
            item['active'] = True
    return {"cabinet_menu": menu}


class LoginView(View):
    pass
class LogoutView(View):
    pass
class ProfileView(View):
    pass
