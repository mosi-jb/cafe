from rest_framework import viewsets

from menu.models import Category, Product, CategoryImage
from menu.serializers.front import CategoryFrontSerializer, ProductFrontSerializer, CategoryImageFrontSerializer


class CategoryFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryFrontSerializer


class ProductFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFrontSerializer


class CategoryFrontImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageFrontSerializer
