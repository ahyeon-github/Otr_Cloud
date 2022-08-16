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

    path("register/", views.RegisterAPIView.as_view()),
    path("auth/", views.AuthView.as_view()), #로그인하기
]