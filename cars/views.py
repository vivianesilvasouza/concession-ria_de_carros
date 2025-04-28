from django.shortcuts import render
from cars.models import Car

# def cars_view(request):
#     cars = Car.objects.all()
#     return render(request, 'cars.html',{'cars': cars}) 

def cars_view(request):
    cars = Car.objects.filter(brand__name='Ford')
    return render(request, 'cars.html',{'cars': cars}) 