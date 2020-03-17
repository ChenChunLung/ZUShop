from django.shortcuts import render, redirect
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

def post(request):
    if request.method == "POST":
        mess = request.POST['username']
    else:
        mess = "Form Data not send yet"
    return render(request, "post.html", locals())  

def post1(request):
    if request.method == "POST":
        cName = request.POST['cName']
        cSex = request.POST['cSex']
        cBirthday = request.POST['cBirthday']
        cEmail = request.POST['cEmail']
        cPhone = request.POST['cPhone']
        cAddr = request.POST['cAddr']

        unit = student.objects.create(cName=cName, cSex=cSex,
                                      cBirthday=cBirthday, cEmail=cEmail, 
                                      cPhone=cPhone, cAddr=cAddr)
        unit.save()
        return redirect('/index/')
    else:
        message = "Please Input Data"
        return render(request, "post1.html", locals())


def index(request):
    return render(request, "index.html", locals())


def handler500(request):
    response = render(request, "error_page/500-error-page.html")
    response.status_code = 500
    return response

        


