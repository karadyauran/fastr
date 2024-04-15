from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(
            user_id=validated_data['user_id'],
            product_id=validated_data['product_id'],
            total_price=validated_data['total_price'],
        )

        order.save()
        return order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        order_item = OrderItem.objects.create(
            order_id=validated_data['order_id'],
            product_id=validated_data['product_id'],
            quantity=validated_data['quantity'],
            price=validated_data['price'],
        )

        order_item.save()
        return order_item
