from rest_framework import serializers
from .models import QuestionSeven, AnswerSeven


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionSeven
        fields = ('title', 'subtitle')
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerSeven
        fields = ('body',)

        
    