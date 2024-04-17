from rest_framework import serializers
from cart.cart_app.models.cart_model import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        cart = Cart.objects.create(**validated_data)

        cart.save()
        return cart
