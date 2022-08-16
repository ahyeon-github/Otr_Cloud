from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import YuseoSerializer, YuseoListSerializer
from .models import Yuseo
from django.http import Http404
from rest_framework.parsers import FileUploadParser


class YuseoOne(APIView):
    def get(self, request):
        yuseos = Yuseo.objects.filter(id__in=[1])

        serializer = YuseoListSerializer(yuseos, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = YuseoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class YuseoTwo(APIView):
    def get(self, request):
        yuseos = Yuseo.objects.filter(id__in=[2])
        
        serializer = YuseoListSerializer(yuseos, many=True)
        return Response(serializer.data)
    
    def post (self , request):
        serializer = YuseoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class YuseoDetail(APIView):
    def get_object(self, pk):
        try:
            return Yuseo.objects.get(pk=pk)
        except Yuseo.DoesNotExist:
            raise Http404
        
        
    def get(self, request, pk):
        yuseo = self.get_object(pk)
        serializer = YuseoSerializer(yuseo)
        return Response(serializer.data)
    
    
    def put (self, request, pk):
        blog = self.get_object(pk)
        serializer = YuseoSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete (self, request, pk):
        yuseo = self.get_object(pk)
        yuseo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UploadView(APIView):
    parser_classes = (FileUploadParser, )
    
    def post(self, request):
        file = request.data.get('file', None)
        import pdb; pdb.set_trace()
        print(file)
        if file:
            return Response({'message': "File is recieved"}, status=200)
        else:
            return Response({'message': "File is missing"}, status=200)



""" class FileView(ModelViewSet):
    queryset= File.objects.all()
    serializer_class= FileSerializer

    def create(self, request, *args, **kwargs):
        return super(FileViewSet, self).create(request, *args, **kwargs) """