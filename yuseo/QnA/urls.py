from django.urls import path
from QnA import views

urlpatterns = [
    path('', views.seven, name="seven"),
    path('question/', views.question, name='question'),
    path('detail/<int:question_id>', views.detail, name='question_detail'),
    path('answercreate/<int:question_id>', views.answercreate, name='answercreate'),
]
