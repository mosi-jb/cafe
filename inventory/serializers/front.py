from rest_framework import serializers

from inventory.models import StockRecord


class StockRecordFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRecord
        fields = '__all__'
