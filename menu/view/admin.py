from rest_framework import viewsets

from menu.models import Category, Product, CategoryImage
from menu.serializers.admin import CategorySerializer, ProductSerializer, CategoryImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryImageViewSet(viewsets.ModelViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer
