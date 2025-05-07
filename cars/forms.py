from django import forms
from .models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200, label='Model', required=True)
    brand = forms.ModelChoiceField(Brand.objects.all(), label='Brand', required=True)
    factory_year = forms.IntegerField(label='Factory Year', required=False)
    model_year = forms.IntegerField(label='Model Year', required=False)
    plate = forms.CharField(max_length=10, label='Plate', required=False)
    price = forms.DecimalField(max_digits=8, decimal_places=2, label='Price', required=False)
    photo = forms.ImageField(label='Photo', required=False)
    
    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            price=self.cleaned_data['price'],
            photo=self.cleaned_data['photo']
        )
        car.save()
        return car