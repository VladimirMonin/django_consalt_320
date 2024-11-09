from django.views.generic import ListView
from core.models import Visit
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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


class LoginView(BaseLoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('users:new_visits')
    redirect_authenticated_user = True

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy('main')

class ProfileNewVisitsListView(LoginRequiredMixin, ListView):
    model = Visit
    template_name = 'visits_list.html'
    context_object_name = 'visits'
    
    def get_queryset(self):
        return Visit.objects.filter(status=0)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Новые заявки'
        context.update(get_cabinet_menu_context(self.request.path))
        return context