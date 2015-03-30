# This file copies the data from data.sfgoc.org for our own use

import json
import urllib2
from trucks.models import Truck

truck_data = urllib2.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json')

truck_json_data = json.load(truck_data)

for truck_json in truck_json_data:
    try:
        truck_id = int(truck_json.get('objectid'))
        truck = Truck.objects.get(id=truck_id)
        truck.id = truck_id
        truck.name = truck_json.get('applicant')
        location = truck_json.get('location')
        if location is not None: truck.latitude = truck_json.get('latitude')
        if location is not None: truck.longitude = truck_json.get('longitude')
        truck.address = truck_json.get('address')
        truck.fooditems  = truck_json.get('fooditems')

        # Catch null / ill-defined trucks
        if  truck.name      is None or \
            truck.latitude  is None or \
            truck.longitude is None or \
            truck.address   is None or \
            truck.fooditems is None :
            continue
        else:
            truck.save()


    except Truck.DoesNotExist, IntegrityError: continue
