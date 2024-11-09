from django.urls import path
from . import views

app_name = 'cabinet' # Имя для пространства имён
"""
Теперь к урлам этого приложения мы будем обращаться как cabinet:login
"""

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('new-visits/', views.ProfileNewVisitsListView.as_view(), name='new_visits'),
]
