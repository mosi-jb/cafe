from rest_framework import serializers

from inventory.models import StockRecord


class StockRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRecord
        fields = '__all__'
