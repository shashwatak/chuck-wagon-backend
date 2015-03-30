from django.shortcuts import render
from django.http import HttpResponse

from .models import Truck

LAT_LONG_FUZZ = 0.005797101448 # approx .4 miles

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def trucks(request):
    trucks = Truck.objects.all()

    return render(request, 'trucks.html', {'trucks': trucks})

def nearby_trucks(request, lat, long):
    lat = float(lat)
    long = float(long)
    print "lat: ", lat, "long: ", long
    trucks = Truck.objects.filter(
        latitude__range = (lat-LAT_LONG_FUZZ, lat+LAT_LONG_FUZZ)
    ).filter(
        longitude__range = (long-LAT_LONG_FUZZ, long+LAT_LONG_FUZZ)
    )


    return render(request, 'trucks.html', {'trucks': trucks})
