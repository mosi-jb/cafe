from rest_framework import viewsets

from inventory.models import StockRecord
from inventory.serializers.front import StockRecordFrontSerializer


class StockRecordFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockRecord.objects.all()
    serializer_class = StockRecordFrontSerializer
