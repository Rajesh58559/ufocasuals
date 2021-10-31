from rest_framework import serializers
from ufo_admin.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'CategoryId', 'CategoryName', 'CategoryDescription', 'CetegoryImage', 'CategoryCreated', 'CategoryUpdated')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('ProductId', 'ProductName', 'Category', 'Price', 'StrikedPrice', 'ProductDescription',
                  'Stock', 'ProductImage1', 'ProductImage2', 'ProductImage3', 'Available', 'ProductCreated',
                  'ProductUpdated'
                  )
