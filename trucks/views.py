from django.shortcuts import render
from django.http import HttpResponse

from .models import Truck

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def trucks(request):
    trucks = Truck.objects.all()

    return render(request, 'trucks.html', {'trucks': trucks})
