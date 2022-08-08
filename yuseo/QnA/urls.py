from django.urls import path
from QnA import views

urlpatterns = [
    path('', views.seven, name="seven"),
]
