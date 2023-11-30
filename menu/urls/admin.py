from rest_framework.routers import SimpleRouter

from menu.view.admin import CategoryViewSet, ProductViewSet, CategoryImageViewSet

router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('categoryImage', CategoryImageViewSet)

urlpatterns = [] + router.urls
