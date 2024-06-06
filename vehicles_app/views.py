from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Vehicle
from .forms import VehicleForm

# all objects from DB
def main_page(request):
    form = VehicleForm()
    vehicles = Vehicle.objects.all()
    
    return render(request, 'MainPage.html', {'form': form, 'vehicles': vehicles})

# create vehicle
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Vehicle created successfully!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    else:
        form = VehicleForm()
    return render(request, 'PopupContent.html', {'form': form, 'action': '등록'})

