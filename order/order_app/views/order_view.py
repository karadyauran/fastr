from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, F

from order.order_app.models.order_model import Order
from order.order_app.models.order_item_model import OrderItem
from order.order_app.serializers.order_serializer import OrderSerializer
from order.order_app.serializers.order_item_serializer import OrderItemSerializer
from order.order_app.utils import get_user_id


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get(request):
    """ Get order items """
    user_id = get_user_id(request=request)
    order = Order.objects.filter(user_id=user_id)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def create(token):
    user_id = get_user_id(token=token)

    serializer = OrderSerializer(data={
        'user': user_id,
    })

    if serializer.is_valid():
        order_instance = serializer.save()
        return order_instance

    return None


def calculate_total_price(order_id):
    """ Calculate total price of order items """
    order_items = OrderItem.objects.filter(order=order_id)
    total_price = order_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0
    order = get_object_or_404(Order, id=order_id)
    order.set_total_price(total=total_price)
    order.save()
    print(order)
    order_items = order_items.select_related('product')
    return Response(OrderItemSerializer(order_items, many=True).data, status=status.HTTP_200_OK)
