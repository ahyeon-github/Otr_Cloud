from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'templates/users/hello.html')