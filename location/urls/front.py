from django.urls import path
from rest_framework.routers import SimpleRouter

from location.view.front import ChairFrontViewSet, LocationFrontViewSet, LocationFrontImageViewSet

router = SimpleRouter()
router.register('location', LocationFrontViewSet)
router.register('chair', ChairFrontViewSet)
router.register('LocationImage', LocationFrontImageViewSet)

urlpatterns = [] + router.urls
