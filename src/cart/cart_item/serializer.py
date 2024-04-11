from rest_framework import serializers
from .models import CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        product = CartItem.objects.create(
            user_id=validated_data['user_id'],
            product_id=validated_data['product_id'],
            quantity=validated_data['quantity'],
        )

        product.save()
        return product
