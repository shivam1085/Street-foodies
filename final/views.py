from django.shortcuts import render
import sqlite3
import random

#from product.models import Food
from product.models import Blog
from django.contrib.auth.models import User,auth
from product.models import Vendor
from django.core.mail import send_mail
from final.settings import EMAIL_HOST_USER
from product.models import Appuser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render(request,"index.html")
def qrvisit(request):
    id=request.GET['id']
    result = Vendor.objects.filter(id__contains=id)
    reward=random.randint(0,20)
    t = Vendor.objects.get(id=id)
            # print(t.title)
    t.reward = t.reward+reward  # change field
    t.save()
    # result = Food.objects.get(id=ids)
    # print(ids)
    print(result)
    return render(request,'qrprofile.html',{'objs':result,'reward':reward})
    # return render(request,'visit.html',{'objs':result})
def visit(request):
    ids=request.GET['ids']
    result = Vendor.objects.filter(id__contains=ids)
    # result = Food.objects.get(id=ids)
    print(ids)
    print(result)
    return render(request,'visit.html',{'objs':result})
def contact(request):
    return render(request,'contact.html') 
def about_us(request):
    return render(request,'about_us.html') 
def blog(request):
    objs=Blog.objects.all()
    return render(request,'blog.html',{'objs':objs}) 
    
def query(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        mes=name+"\n"+email+'\n'+message
        print(name,email,message)
        send_mail("foodies query",mes, EMAIL_HOST_USER, ["streetfoodies20@gmail.com"], fail_silently = False)
        print(name,email,message)
    return render(request,'tq.html')
    
    # return render(request,'tq.html')
def vendor(request):  #for vendor login purpose
    return render(request,'vlogin.html')
def vlogin(request):
    if(request.method=="POST"):
        mobile=request.POST['mobile']
        password=request.POST['password']
        if(Vendor.objects.filter(mobile=mobile, password=password).exists()):
        # print(name)
            result=Vendor.objects.filter(mobile=mobile, password=password)
            print(result)
            return render(request,'profile.html',{'objs':result})
        else:
            return render(request,'vlogin.html')
def appuser(request):
    return render(request,'ulogin.html')
def register(request):
    return render(request,'register.html')
def signup(request): #user register
    if(request.method=="POST"):
        try:
        # fristname=request.POST['fristname']
        # lastname=request.POST['lastname']
        # email=request.POST['email']
        # password=request.POST['password']
            app=Appuser()
            app.mobile= request.POST.get('mobile')
            app.password= request.POST.get('password')
            app.save()
        
            print("user created")        
            return render(request,'ulogin.html')
        except:
            return render(request,'register.html')
        

    else:
        return render(request,'register.html')
def ulogin(request): #user signin
    if(request.method=="POST"):
        mobile=request.POST['mobile']
        password=request.POST['password']
        if(Appuser.objects.filter(mobile=mobile, password=password).exists()):
        # print(name)
            result=Appuser.objects.filter(mobile=mobile, password=password)
            print(result)
            # print(result)
            return render(request,'userprofile.html',{'objs':result})
        else:
            return render(request,'ulogin.html')