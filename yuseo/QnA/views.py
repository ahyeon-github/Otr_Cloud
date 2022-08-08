from django.shortcuts import render

# Create your views here.
def seven(request):
    return render(request, 'QnA/seven.html')