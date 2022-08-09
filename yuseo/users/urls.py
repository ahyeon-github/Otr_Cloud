"""from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
]"""

from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.createUser),
    path('login/', views.login),
]