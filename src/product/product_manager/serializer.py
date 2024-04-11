from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            image=validated_data['image'],
            stock=validated_data['stock'],
        )

        product.save()
        return product
