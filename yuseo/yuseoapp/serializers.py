from asyncio import Task
from dataclasses import field, fields
from rest_framework import serializers
from .models import Yuseo 



 

class YuseoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Yuseo
        fields = ('id', 'title', 'date', 'body', 'image')
        
class YuseoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yuseo
        fields = ('id', 'title', 'date', 'summary')
        
        
        
 