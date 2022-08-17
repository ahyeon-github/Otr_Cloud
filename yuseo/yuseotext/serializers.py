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
        fields = ('id', 'title', 'date', 'time', 'body')
        
class YuseoTextListSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = YuseoText
        fields = ('id', 'title', 'date', 'time', 'body')        # body 추가


        