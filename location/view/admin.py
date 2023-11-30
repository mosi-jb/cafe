from rest_framework import viewsets

from location.models import Location, Chair, LocationImage
from location.serializers.admin import LocationSerializer, ChairSerializer, LocationImageSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ChairViewSet(viewsets.ModelViewSet):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer


class LocationImageViewSet(viewsets.ModelViewSet):
    queryset = LocationImage.objects.all()
    serializer_class = LocationImageSerializer
