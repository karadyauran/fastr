from rest_framework import serializers
from cart.cart_app.models.cart_item_model import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        product = CartItem.objects.create(
            cart_id=validated_data['cart_id'],
            product_id=validated_data['product_id'],
            quantity=validated_data['quantity'],
        )

        product.save()
        return product
