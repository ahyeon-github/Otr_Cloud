from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def seven(request):
    return render(request, 'QnA/seven.html')

def question(request):
    questions= Question.objects
    return render(request, 'QnA/question.html', {'questions':questions})

def detail(request, question_id):
    question_detail= get_object_or_404(Question, pk= question_id)
    return render(request, 'QnA/detail.html', {'question': question_detail})