from django.shortcuts import redirect, render
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    
    return render(request, 'cars.html',{'cars': cars}) 

def new_car_view(request):
    if request.method == 'POST':
        new_car = CarModelForm(request.POST, request.FILES)
        if new_car.is_valid():
            new_car.save()
            return redirect('cars_list')
    else:
        new_car = CarModelForm()
    return render(request, 'new_car.html',{'new_car': new_car}) 

