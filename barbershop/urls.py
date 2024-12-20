"""
URL configuration for barbershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.views import (
    ServicesByMasterView,
    MainView,
    ThanksTemplateView,
    ReviewCreateView,
    ReviewThanksTemplateView,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cabinet/', include('users.urls', namespace='users')), # namespace - указываем его из urls.py
    path("", MainView.as_view(), name="main"),
    path("thanks/", ThanksTemplateView.as_view(), name="thanks"),
    path(
        "get_services_by_master/<int:master_id>/",
        ServicesByMasterView.as_view(),
        name="get_services_by_master",
    ),
    path("review/create/", ReviewCreateView.as_view(), name="review_create"),
    path("review/thanks/", ReviewThanksTemplateView.as_view(), name="review_thanks"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
