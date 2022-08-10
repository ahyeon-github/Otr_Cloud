from django.urls import path


from .views import Question, Answer

urlpatterns = [
   path('question/', Question.as_view()),
   path('answer/', Answer.as_view())
]
