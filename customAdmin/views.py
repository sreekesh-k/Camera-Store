from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import for displaying messages to the user

def login(request):
    return render(request, "login.html")

def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('admindash')

    if request.method == 'POST':
        username = request.POST.get("name")
        password = request.POST.get("password")

        # Check if either the username or password is empty
        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return render(request, "adminLogin.html", {'username': username})

        user = authenticate(username=username, password=password)  # Authenticate the user directly
        if user is not None and user.is_superuser:
            auth_login(request, user)
            return redirect('admindash')
        else:
            messages.error(request, "Invalid username or password.")  # Display error message
            return render(request, "adminLogin.html", {'username': username})  # Keep the username field populated

    return render(request, "adminLogin.html")  # Handle GET request or other non-POST methods

@login_required
def admindash(request):
    if request.user.is_superuser:
        pagehead = "Dashboard"
        return render(request, "admindashboard.html",{"pagehead":pagehead})
    else:
        return redirect('adminlogin') 
    
def adminlogout(request):
    logout(request)
    return redirect('login')