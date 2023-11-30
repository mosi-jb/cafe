from rest_framework import serializers

from location.models import Location, Chair, LocationImage


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'


class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = '__all__'
