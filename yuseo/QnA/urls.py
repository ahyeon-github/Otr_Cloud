from django.urls import path
from QnA.views import Question, Answer, AnswerTwo, AnswerThree, AnswerFour, AnswerFive, AnswerSix, AnswerLast, AnswerAll

urlpatterns = [
   path('question/', Question.as_view()),
   path('answer1/', Answer.as_view()),
   path('answer2/', AnswerTwo.as_view()),
   path('answer3/', AnswerThree.as_view()),
   path('answer4/', AnswerFour.as_view()),
   path('answer5/', AnswerFive.as_view()),
   path('answer6/', AnswerSix.as_view()),
   path('answer7/', AnswerLast.as_view()),
   path('answerall/', AnswerAll.as_view()),
]

