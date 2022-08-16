from asyncio import Task
from dataclasses import field, fields
from msilib.schema import File
from stat import FILE_ATTRIBUTE_SYSTEM
# from typing_extensions import Required
from rest_framework import serializers
from .models import Yuseo 


class YuseoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    voice = serializers.FileField(use_url=True)
    video = serializers.FileField(use_url=True)
    
    class Meta:
        model = Yuseo
        fields = ('id', 'title', 'date', 'body', 'image', 'voice', 'video')
        
class YuseoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yuseo
        fields = ('id', 'title', 'date', 'summary')
        
        
""" class FileSerializer(serializers.ModelSerializer):
    path= serializers.FileField(required=False)

    class Meta:
        model = File
        fields = '__all__'
        read_only_fields =('id', ) """