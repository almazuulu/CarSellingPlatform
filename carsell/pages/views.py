from django.shortcuts import render
from .models import Team
from cars.models import Car, CarsPost

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
    return render(request, 'pages/contact.html')