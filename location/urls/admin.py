from django.urls import path
from rest_framework.routers import SimpleRouter

from location.view.admin import LocationViewSet, ChairViewSet, LocationImageViewSet

router = SimpleRouter()
router.register('location', LocationViewSet)
router.register('chair', ChairViewSet)
router.register('LocationImage', LocationImageViewSet)

urlpatterns = [] + router.urls
