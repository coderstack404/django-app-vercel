from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    message = "Salom hammaga!"
    return HttpResponse(message)