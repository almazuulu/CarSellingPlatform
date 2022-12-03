from django.urls import path
from .views import cars, car_detail, search

urlpatterns = [
    path('', cars, name='cars'),
    path('search', search, name='search'),
    path('<str:id>', car_detail, name='car_detail'),
    
]