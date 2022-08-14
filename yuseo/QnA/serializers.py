from rest_framework import serializers
from .models import QuestionSeven, AnswerSeven


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionSeven
        fields = ('id', 'title', 'subtitle')
        

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerSeven
        fields = ('q_id', 'body',)

"""     def to_representation(self, instance):
        self.fields['q_id']= QuestionRepresentationSerializer(read_only=True)
        return super(AnswerSerializer, self).to_representation(instance) """

    
""" class QuestionRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuestionSeven
        fields=("id", "title", "subtitle", "body") """
        