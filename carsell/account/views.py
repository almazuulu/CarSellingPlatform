from django.shortcuts import render


def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'account/logout.html')

def register(request):
    return render(request, 'account/register.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')