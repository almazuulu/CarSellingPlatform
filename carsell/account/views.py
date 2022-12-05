from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return render(request, 'account/logout.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'This user already exists')
                return redirect('register')
            else:
                user = User.objects.create(first_name=firstname, last_name=lastname,email=email, username=username, password=password)     
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard')
                user.save()
                messages.success(request, 'User has been successfully registered!')
                return redirect('login') 
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
        # messages.error(request, 'Could not register')
       
    else:
        return render(request, 'account/register.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')