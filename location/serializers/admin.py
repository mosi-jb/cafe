from rest_framework import serializers

from location.models import Location, Chair, LocationImage


class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'


class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    chairs = ChairSerializer(read_only=True, many=True)
    picture = LocationImageSerializer(read_only=True, many=True)

    class Meta:
        model = Location
        fields = '__all__'
