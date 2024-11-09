from django.urls import path
from . import views

app_name = 'users' # Имя для пространства имён
"""
Теперь к урлам этого приложения мы будем обращаться как users:login
"""

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
