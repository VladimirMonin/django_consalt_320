from django.urls import path
from . import views

app_name = 'cabinet' # Имя для пространства имён
"""
Теперь к урлам этого приложения мы будем обращаться как cabinet:login
"""

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('all-visits/', views.ProfileVisitsListView.as_view(), name='all_visits'),
    path('new-visits/', views.ProfileVisitsListView.as_view(), {'visit_type': 'new'}, name='new_visits'),
    path('visit-archive/', views.ProfileVisitsListView.as_view(), {'visit_type': 'archive'}, name='visit_archive'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),

]