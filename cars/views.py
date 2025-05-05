from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    
    return render(request, 'cars.html',{'cars': cars}) 

def new_car_view(request):
    new_car = CarForm()
    
    return render(request, 'new_car.html',{'new_car': new_car}) 

# def cars_view(request):
#     cars = Car.objects.filter(brand__name='Ford')
#     return render(request, 'cars.html',{'cars': cars}) 