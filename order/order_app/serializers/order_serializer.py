from rest_framework import serializers
from order.order_app.models.order_model import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)

        order.save()
        return order
