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
        
        
        
        
"""class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image',)


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    images = TaskImageSerializer(source='taskimage_set', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'date', 'body', 'images')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        task = Task.objects.create(title=validated_data.get('title', 'no-title'),
                                   user_id=1)
        for image_data in images_data.values():
            TaskImage.objects.create(task=task, image=image_data)
        return task"""