from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from shop_app.models import student


# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django!!")

def hello3(request):
    now = datetime.now()
    return render(request, "hello3.html", locals())

def dice(request):
    no = random.randint(1,6)
    dict1 = {"name":"Amy","age":20}
    return render(request, "dice.html", locals())

def listone(request):
    try:
        unit = student.objects.get(cName='winnie')
    except:
        errormessage = "Read Error!!"
    return render(request, "listone.html", locals())   

def listall(request):
    students = student.objects.all().order_by('id')
    return render(request, "listall.html", locals())




