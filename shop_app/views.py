from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import random
from shop_app.models import student
from shop_app.form import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth


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

def postform(request):
    postform = PostForm()
    return render(request, "postform.html", locals())

def post2(request):
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            cName = postform.cleaned_data['cName']
            cSex = postform.cleaned_data['cSex']
            cBirthday = postform.cleaned_data['cBirthday']
            cEmail = postform.cleaned_data['cEmail']
            cPhone = postform.cleaned_data['cPhone']
            cAddr = postform.cleaned_data['cAddr']


            unit = student.objects.create(cName=cName, cSex=cSex,
                                      cBirthday=cBirthday, cEmail=cEmail, 
                                      cPhone=cPhone, cAddr=cAddr)
            unit.save()
            message='Saved ....'
            return redirect('/index/')
        else:
            message = 'Validate Code Error!!'
    else:
        message = "Name,Sex, Birthday must Input"
        postform = PostForm()
    return render(request, "post2.html", locals())  

def delete(request, id=None):
    if id != None:
        if request.method == "POST":
            id = request.POST['cId']
            try:
                unit = student.objects.get(id=id)
                unit.delete()
                return redirect('/index/')
            except:
                message = "Read Error"

    return render(request, "delete.html", locals())

def edit(request,id=None,mode=None):
    if mode == "edit":
        unit = student.objects.get(id=id)
        unit.cName = request.GET['cName']
        unit.cSex = request.GET['cSex']
        unit.cBirthday = request.GET['cBirthday']
        unit.cEmail = request.GET['cEmail']
        unit.cPhone = request.GET['cPhone']
        unit.cAddr = request.GET['cAddr']

        unit.save()
        message='Saved ....'
        return redirect('/index/')
       
    else:
        try:
            unit = student.objects.get(id=id)
            strdate = str(unit.cBirthday)
            strdate2 = strdate.replace("年", "-")
            strdate2 = strdate.replace("月", "-")
            strdate2 = strdate.replace("日", "-")
            unit.cBirthday = strdate2    
        except:    
	        message = "This Id is not exist"
    
    return render(request, "edit.html", locals())

def adduser(request):
    try:
        user = User.objects.get(username="test")
    except:    
        user = None
        if user != None:
            message = user.username + "Account Has Created!!"
            return HttpResponse(message)
        else:
            user = User.objects.create_user("test", "test@test.com.tw", "aa123456")
            user.first_name = "wen"
            user.last_name = "lin"
            user.is_staff = True
            user.save()
            return redirect('/admin/')

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                #return redirect("/index/")
                message = "Login Success"
                return render(request, "index.html", locals())
            else:
                message = "Account is not enable"
        else:
            message = "Login Failed"

    return render(request, "login.html", locals())

def logout(request):
    auth.logout(request)
    return redirect("/index/")


def handler500(request):
    response = render(request, "error_page/500-error-page.html")
    response.status_code = 500
    return response

        


