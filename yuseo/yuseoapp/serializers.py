from dataclasses import field
from rest_framework import serializers
from .models import Yuseo

class YuseoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yuseo
        fields = ('id', 'title', 'date', 'body')
        
class YuseoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yuseo
        fields = ('id', 'title', 'date', 'summary')
        
        