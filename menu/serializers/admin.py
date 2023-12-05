from rest_framework import serializers

from inventory.serializers.admin import StockRecordSerializer
from menu.models import Category, Product, CategoryImage


class ProductSerializer(serializers.ModelSerializer):
    stockrecords = StockRecordSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    picture = CategoryImageSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'
