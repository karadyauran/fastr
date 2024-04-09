from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category']

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
        )

        if 'description' in validated_data:
            product.description = validated_data['description']

        if 'category' in validated_data:
            product.category = validated_data['category']

        product.save()
        return product
