from django.shortcuts import render
from django.http import HttpResponse

from .models import Truck

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def db(request):

    # truck = Truck()
    # truck.save()

    trucks = Truck.objects.all()

    return render(request, 'db.html', {'trucks': trucks})
