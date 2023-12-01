from rest_framework import viewsets

from inventory.models import StockRecord
from inventory.serializers.admin import StockRecordSerializer


class StockRecordViewSet(viewsets.ModelViewSet):
    queryset = StockRecord.objects.all()
    serializer_class = StockRecordSerializer
