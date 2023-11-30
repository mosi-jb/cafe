from rest_framework import serializers

from menu.models import Category, Product, CategoryImage


class CategoryFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryFrontImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'
