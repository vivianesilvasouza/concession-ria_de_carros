from django.contrib import admin
from cars.models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
class CarAdmin(admin.ModelAdmin):
    list_display = ( 'model', 'brand', 'factory_year', 'model_year', 'formatted_price')
    search_fields = ('model', 'brand')
    
    def formatted_price(self, obj):
        if obj.price is not None:
            return f'R$ {obj.price:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        return "-"
    formatted_price.short_description = 'Price'

admin.site.register(Brand, BrandAdmin)   
admin.site.register(Car, CarAdmin)
