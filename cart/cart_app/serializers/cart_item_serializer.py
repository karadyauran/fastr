from rest_framework import serializers
from cart.cart_app.models.cart_item_model import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        cart_item = CartItem.objects.create(**validated_data)

        cart_item.save()
        return cart_item
