from django.urls import path
from .views import main_page, vehicle_create

urlpatterns = [
    path("", main_page, name='MainPage'),
    path('vehicle_create/', vehicle_create, name='vehicle_create')
]
