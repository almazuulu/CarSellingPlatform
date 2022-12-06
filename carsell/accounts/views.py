from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from cars.models import Car


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This user already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists')
                    return redirect('register')
                else:        
                    user = User.objects.create_user(first_name=firstname, last_name=lastname,email=email, username=username, password=password)     
                    user.save()
                    messages.success(request, 'User has been successfully registered!')
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('dashboard')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
        # messages.error(request, 'Could not register')
       
    else:
        return render(request, 'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
    user_id = request.user.id
    allInquires = Contact.objects.order_by('created_date').filter(user_id=user_id)
    carList = [i.car_id for i in allInquires]
    carListView = []
    
    for cl in carList:
        car = Car.objects.get(id=cl)
        carListView.append(car)
        
    context = {
        'allInquires': allInquires,
        'cars': carListView,
    }

    return render(request, 'accounts/dashboard.html', context)