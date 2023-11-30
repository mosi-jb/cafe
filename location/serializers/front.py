from rest_framework import serializers

from location.models import Location, Chair, LocationImage


class LocationFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ChairFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'


class LocationFrontImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = '__all__'
