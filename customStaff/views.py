from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm

from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authenticate user
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                # Redirect to a success page, or wherever you want
                return redirect('staffdashboard')
            else:
                # Authentication failed, display error message
                messages.error(request, "Invalid email or password.")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})