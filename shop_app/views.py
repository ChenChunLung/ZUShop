from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django!!")

def hello3(request):
    now = datetime.now()
    return render(request, "hello3.html", locals())


