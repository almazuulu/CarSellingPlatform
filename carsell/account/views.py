from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'account/logout.html')

def register(request):
    if request.method == 'POST':
        messages.error(request, 'Could not register')
        return redirect('register')
    else:
        return render(request, 'account/register.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')