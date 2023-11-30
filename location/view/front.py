from rest_framework import viewsets

from location.models import Location, Chair, LocationImage
from location.serializers.front import LocationFrontSerializer, ChairFrontSerializer, LocationFrontImageSerializer


class LocationFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationFrontSerializer


class ChairFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chair.objects.all()
    serializer_class = ChairFrontSerializer


class LocationFrontImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LocationImage.objects.all()
    serializer_class = LocationFrontImageSerializer
