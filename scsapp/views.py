from django.shortcuts import render,redirect
from .models import Dept,Emp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.http import HttpResponse
import requests
def home(request):
    return render(request,"scsapp/home.html")

def aboutus(request):
    response = requests.get('http://127.0.0.1:8000/tutors')	
    tutor = response.json()
    return render(request,"scsapp/aboutus.html",{"data":tutor})

def gallery(request):
   
    if request.method=="POST":
       data = {"username":request.POST.get("txtuser"),"password":request.POST.get("txtpass"),"mobileno":request.POST.get("txtmobile"),"fname":request.POST.get("txtfname")}
       response = requests.post('http://127.0.0.1:8000/tutors',data)	
       s=''
       #print("status code is ",response.status_code)
       if response.status_code == 201:
        s='data inserted successfully'
       else:
        s ='data not inserted successfully'
       return render(request,"scsapp/gallery.html",{'key':s})
    else:
        return render(request,"scsapp/gallery.html")

def contactus(request):
    data = {"username":"test12333","password":"11111","mobileno":"888988122","fname":"manish kumar"}
    response = requests.put('http://127.0.0.1:8000/tutors/1',data)	
    s=''
    print("status code is ",response.status_code)
    if response.status_code == 200:
        s='data updated successfully'
        return render(request,"scsapp/contactus.html",{"key":s})
    else:
        s ='data not updated successfully'
        return render(request,"scsapp/contactus.html",{"key":s})

def services(request):
    response = requests.delete('http://127.0.0.1:8000/tutors/5')	
    s=''
    print("status code is ",response.status_code)
    if response.status_code == 204:
        return redirect("/scsapp/aboutus")
    else:
       return render(request,"scsapp/services.html")

def managedept(request):
    pass

def manageemp(request):
    d = Dept.objects.get(pk=2)
    res = d.emp_set.all() # display employee of deptid 1
    return render(request,"scsapp/viewemp.html",{"key":res})
def managereg(request):
     user = User.objects.create_user('testuser1','testuser1@gmail.com','12345678')
     user.first_name='ram'
     user.last_name='kumar'
     user.save()
     return HttpResponse("User Registration Successfully")
def managelogin(request):
    obj = authenticate(username='testuser1',password='12345678')
    if obj is not None:
        login(request,obj)
        return HttpResponse("login Successfully")
    else:
        return HttpResponse("login failed")
def managelogout(request):
     logout(request)
     return HttpResponse("logout successfully")