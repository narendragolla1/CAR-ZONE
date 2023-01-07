from django.shortcuts import render
from .models import Car
# Create your views here.
def cars(request):
    
    return render(request,'cars/cars.html')