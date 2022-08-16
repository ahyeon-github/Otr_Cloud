from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from .models import QuestionSeven, AnswerSeven
from .serializers import QuestionSerializer, AnswerSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# from users.models import date_joined

class Question(APIView):
    def get(self, request):
        questions = QuestionSeven.objects.all()
        
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = QuestionSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Answer(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.filter(q_id__in=[1])    

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerTwo(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.filter(q_id__in=[2])    

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AnswerThree(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.filter(q_id__in=[3])    

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class AnswerFour(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.filter(q_id__in=[4])    

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class AnswerFive(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.filter(q_id__in=[5])    

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class AnswerSix(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.filter(q_id__in=[6])    

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AnswerLast(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.filter(q_id__in=[7])    

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerAll(APIView):
    def get(self, request):
        answers = AnswerSeven.objects.all()

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = AnswerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)