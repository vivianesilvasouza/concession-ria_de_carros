from django import forms
from .models import Brand, Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__' # ele vai pegar todos os campos do model
        