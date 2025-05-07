from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cars.views import cars_view, new_car_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_view, name='cars_list'),
    path('new_car/', new_car_view, name='new_car_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
