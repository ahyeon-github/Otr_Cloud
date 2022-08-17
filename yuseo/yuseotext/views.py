from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import YuseoTextSerializer, YuseoTextListSerializer
from .models import YuseoText


class YuseoOne(APIView):
    def get(self, request):
        yuseos = YuseoText.objects.filter(id__in=[1])

        serializer = YuseoTextListSerializer(yuseos, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = YuseoTextSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class YuseoTwo(APIView):
    def get(self, request):
        yuseos = YuseoText.objects.filter(id__in=[2])
        
        serializer = YuseoTextListSerializer(yuseos, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = YuseoTextSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class YuseoThree(APIView):
    def get(self, request):
        yuseos = YuseoText.objects.filter(id__in=[3])
        
        serializer = YuseoTextListSerializer(yuseos, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = YuseoTextSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)