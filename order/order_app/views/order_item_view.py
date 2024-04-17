from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from order.order_app.models.order_item_model import OrderItem
from order.order_app.serializers.order_item_serializer import OrderItemSerializer
from cart.cart_app.utils.utils import get_user_id, check_product
from order.order_app.utils import get_order_id
from order.order_app.views.order_view import calculate_total_price


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add(request):
    # TODO: make it for cart
    """ Add all order items from cart """
    user_id = get_user_id(request=request)
    product_id = request.data.get('product_id')
    if not product_id or not check_product(product_id):
        return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    quantity = request.data.get('quantity', 1)
    order_item, created = OrderItem.objects.get_or_create(cart_id=get_order_id(user_id), product_id=product_id,
                                                          defaults={'quantity': quantity})
    if not created and quantity:
        order_item.quantity += int(quantity)
        order_item.save()
    calculate_total_price(get_order_id(user_id))
    return Response(OrderItemSerializer(order_item).data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def edit_order_item_quantity(request):
    """ Edit cart item quantity """
    user_id = get_user_id(request=request)
    cart_id = get_order_id(user_id)
    order_item = get_object_or_404(OrderItem, pk=request.query_params.get('order_id'))
    order_item.quantity = request.data.get('quantity', order_item.quantity)
    order_item.save()
    calculate_total_price(cart_id)
    return Response('OrderItem quantity updated', status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def remove(request):
    """ Remove cart item """
    user_id = get_user_id(request=request)
    order_id = get_order_id(user_id)
    order_item = get_object_or_404(OrderItem, pk=request.query_params.get('order_id'))
    order_item.delete()
    calculate_total_price(order_id)
    return Response('Order item deleted', status=status.HTTP_200_OK)
