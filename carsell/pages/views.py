from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car, CarsPost
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    model_search = Car.objects.values_list('model', flat=True).distinct
    city_search = Car.objects.values_list('city', flat=True).distinct
    year_search = Car.objects.values_list('year', flat=True).distinct
    bs_search = Car.objects.values_list('body_style', flat=True).distinct
    
    all_cars = Car.objects.order_by('-created_date')
    # car_photos = featured_cars.carspost_set.all()
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'bs_search': bs_search,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        message_mail = f'You have message in CarSell from {name} regarding: {message}\
        \n\nSender details: Phone: {phone}; Email: {email};'
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            subject,
            mark_safe(message_mail),
            'askardjango@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been successfully sent!')
        return redirect('contact')

    return render(request, 'pages/contact.html')