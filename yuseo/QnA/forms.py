from socket import fromshare
from django import forms
from .models import Question, Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model= Answer
        fields = ['content']