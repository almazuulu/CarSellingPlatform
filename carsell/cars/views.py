from django.shortcuts import render, get_object_or_404
from .models import Car, CarsPost


# Create your views here.
def cars(request):
    return render(request, 'cars/cars.html')

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    context = {
        'car': car,
    }
    
    return render(request, 'cars/cardetails.html', context)


