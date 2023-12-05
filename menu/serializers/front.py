from rest_framework import serializers

from inventory.serializers.front import StockRecordFrontSerializer
from menu.models import Category, Product, CategoryImage


class ProductFrontSerializer(serializers.ModelSerializer):
    stockrecords = StockRecordFrontSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryImageFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'


class CategoryFrontSerializer(serializers.ModelSerializer):
    product = ProductFrontSerializer(read_only=True, many=True)
    picture = CategoryImageFrontSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'
