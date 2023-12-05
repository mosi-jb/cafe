from rest_framework import serializers

from location.models import Location, Chair, LocationImage


class ChairFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'


class LocationImageFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = '__all__'


class LocationFrontSerializer(serializers.ModelSerializer):
    chairs = ChairFrontSerializer(read_only=True, many=True)
    picture = LocationImageFrontSerializer(read_only=True, many=True)

    class Meta:
        model = Location
        fields = '__all__'
