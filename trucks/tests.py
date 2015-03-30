from django.test import TestCase
from django.test import Client
from trucks.models import Truck

class TruckTestCase(TestCase):
    def setUp(self):
        Truck.objects.create(id=0, name="truckA", latitude=0.0, longitude=0.0)
        Truck.objects.create(id=1, name="truckB", latitude=10.0, longitude=-10.0)

    def test_truck_locations(self):
        truckA = Truck.objects.get(name="truckA")
        truckB = Truck.objects.get(name="truckB")
        self.assertEqual(truckA.latitude, 0.0)
        self.assertEqual(truckB.longitude, -10,0)


class AllViewTestCase(TestCase):
    def test_view_response(self):
        c = Client()
        response = c.get('/trucks')
        self.assertEqual(response.status_code, 200)

class NearbyViewTestCase(TestCase):
    def setUp(self):
        Truck.objects.create(id=0, name="truckA", latitude=0.0, longitude=0.0)
        Truck.objects.create(id=1, name="truckB", latitude=10.0, longitude=-10.0)

    def test_view_response(self):
        c = Client()
        response = c.get('/trucks/0.0/0.0')
        self.assertEqual(response.status_code, 200)
