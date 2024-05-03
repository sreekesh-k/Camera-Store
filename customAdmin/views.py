from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def login(request):
    return render(request,"login.html")

def adminlogin(request):
    return render(request,"adminLogin.html")