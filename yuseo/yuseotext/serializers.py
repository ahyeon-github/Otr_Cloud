from asyncio import Task
from dataclasses import field, fields
from msilib.schema import File
from stat import FILE_ATTRIBUTE_SYSTEM
# from typing_extensions import Required
from rest_framework import serializers
from .models import YuseoText


class YuseoTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = YuseoText
        fields = ('id', 'title', 'date', 'body')
        
class YuseoTextListSerializer(serializers.ModelSerializer):
    class Meta:
        model = YuseoText
        fields = ('id', 'title', 'date')
        