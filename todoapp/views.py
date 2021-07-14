from django.contrib import auth
from django.contrib.auth import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm
from .models import Task



class NewTask(forms.Form):
    task=forms.CharField(label="Task",widget=forms.TextInput(attrs={"class":"form-control",'style': 'width: 300px;'}))
    priority=forms.IntegerField(label="Priority",max_value=10,min_value=1,widget=forms.NumberInput(attrs={"class":"form-control ",'style': 'width: 300px;'}))
    duration=forms.IntegerField(label="Duration in Minutes",min_value=30,widget=forms.NumberInput(attrs={"class":" form-control","min":"30",'style': 'width: 300px;'}))

def homepage(request):
    return render (request,"tasks/homepage.html")

def login_page(request):
    if request.method=="POST":
        usern=request.POST["username"]
        passw=request.POST["password"]
        user=authenticate(request,username=usern,password=passw)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'tasks/login.html',{
                "message":"Invalid Username or Password"
            })
    return render(request,"tasks/login.html")

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def signup(request):
    if request.method=="POST":
        user_form =UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Account created successfully')
            return HttpResponseRedirect(reverse('login'))            
    else:
        user_form = UserForm()
    return render(request,'tasks/signup.html',{
            'form':user_form
        })


def my_tasks(request):
    view_tasks=Task.objects.all()
    # if "list_of_tasks" not in request.session:
    #     request.session["list_of_tasks"]=[]
    return render(request,'tasks/index.html',{
        "all_tasks":view_tasks
    })

    

    # if "list_of_tasks" not in request.session:
    #     request.session["list_of_tasks"]=[]
    # return render(request,'tasks/index.html',{
    #     "all_tasks":request.session["list_of_tasks"]
    # })


def addTask(request):
    if request.method=="POST":
        form_data=NewTask(request.POST)
        if form_data.is_valid():
            # task_entered=form_data.cleaned_data["task"]
            # duration=form_data.cleaned_data["duration"]
            Task.objects.create(
                task=request.POST.get("task"),
                priority=request.POST.get("priority"),
                duration=request.POST.get("duration")

            )
            return HttpResponseRedirect(reverse("index"))
                
            # request.session["list_of_tasks"]+=[f"{task_entered}..............{duration} Mins"]
            # return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"tasks/addtask.html",{"form":form_data})
    
    return render(request,"tasks/addtask.html",{
            "form":NewTask()
        })

    