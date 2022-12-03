from django.shortcuts import render, get_object_or_404
from .models import Car, CarsPost


# Create your views here.
def cars(request):
    allcars = Car.objects.all()
    context = {
        'cars': allcars,
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    context = {
        'car': car,
    }
    
    return render(request, 'cars/cardetails.html', context)


