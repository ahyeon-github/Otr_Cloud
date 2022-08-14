from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# from users.models import date_joined

class Question(APIView):
    def get(self, request):
        questions = Question.objects.all()
        #q= Question.objects.filter(day = day)
        #q= Question.objects.filter(day = date.today - date_joined)

        # 여기서 day가 models.py에 있는 day=models.IntegerField() 인데 import하는 방법이랑 filter 쓸 때 비교하는 방법을 모르겠음.
        
        serializer = QuestionSerializer(q, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = QuestionSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Answer(APIView):
    def get(self, request):
        questions = Answer.objects.all()    
        
        serializer = AnswerSerializer(questions, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
