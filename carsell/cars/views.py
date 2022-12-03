from django.shortcuts import render, get_object_or_404
from .models import Car, CarsPost
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def cars(request):
    allcars = Car.objects.all()
    paginator = Paginator(allcars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    context = {
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    context = {
        'car': car,
    }
    
    return render(request, 'cars/cardetails.html', context)


