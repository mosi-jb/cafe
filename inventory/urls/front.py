from rest_framework.routers import SimpleRouter

from inventory.view.front import StockRecordFrontViewSet

router = SimpleRouter()
router.register('StockRecord', StockRecordFrontViewSet)

urlpatterns = [] + router.urls
