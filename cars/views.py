from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    
    return render(request, 'cars.html',{'cars': cars}) 

# def cars_view(request):
#     cars = Car.objects.filter(brand__name='Ford')
#     return render(request, 'cars.html',{'cars': cars}) 