from rest_framework.routers import SimpleRouter

from inventory.view.admin import StockRecordViewSet

router = SimpleRouter()
router.register('StockRecord', StockRecordViewSet)

urlpatterns = [] + router.urls
