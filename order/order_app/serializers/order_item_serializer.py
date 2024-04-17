from rest_framework import serializers
from order.order_app.models.order_item_model import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        order_item = OrderItem.objects.create(**validated_data)

        order_item.save()
        return order_item
