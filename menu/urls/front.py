from rest_framework.routers import SimpleRouter

from menu.view.front import CategoryFrontViewSet, ProductFrontViewSet, CategoryFrontImageViewSet

router = SimpleRouter()
router.register('category', CategoryFrontViewSet)
router.register('product', ProductFrontViewSet)
router.register('categoryImage', CategoryFrontImageViewSet)

urlpatterns = [] + router.urls
