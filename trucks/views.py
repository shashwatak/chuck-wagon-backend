from django.shortcuts import render
from django.http import HttpResponse

from .models import Truck

LAT_LONG_FUZZ = 0.005797101448 # approx .4 miles
FEET_PER_DEGREE = 364099.0681813498

# Create your views here.
def index(request):
    return render(request, 'hello.html')


def trucks(request):
    trucks = Truck.objects.all()

    return render(request, 'trucks.html', {'trucks': trucks})

def nearby_trucks(request, lat, long):
    lat = float(lat)
    long = float(long)
    trucks = Truck.objects.filter(
        latitude__range = (lat-LAT_LONG_FUZZ, lat+LAT_LONG_FUZZ)
    ).filter(
        longitude__range = (long-LAT_LONG_FUZZ, long+LAT_LONG_FUZZ)
    )

    return render(request, 'trucks.html', {'trucks': trucks})

def trucks_within_distance(request, feet, lat, long):
    feet = float(feet)
    lat = float(lat)
    long = float(long)
    print "feet: ", feet, "lat: ", lat, "long: ", long

    degrees_range = feet / FEET_PER_DEGREE

    trucks = Truck.objects.filter(
        latitude__range = (lat-degrees_range, lat+degrees_range)
    ).filter(
        longitude__range = (long-degrees_range, long+degrees_range)
    )

    return render(request, 'trucks.html', {'trucks': trucks})
