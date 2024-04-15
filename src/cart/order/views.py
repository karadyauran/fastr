from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order.models import Order, OrderItem
from order.serializer import OrderSerializer, OrderItemSerializer


@api_view(['GET'])
def order_list(request):
    """ Get all orders """
    orders = Order.objects.filter(request.query_params.get('order_id'))
    serializer = OrderSerializer(orders, many=True)
    return Response({'orders': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def order_add(request):
    """ Add a new order """
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def order_delete(request):
    """ Delete an order """
    order = get_object_or_404(Order, pk=request.query_params.get('order_id'))
    order.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def order_update(request):
    """ Update an order """
    order = get_object_or_404(Order, pk=request.data['order_id'])

    if order:
        if 'total_price' in request.data:
            order.total_price = request.data['total_price']
            order.save()

        if 'status' in request.data:
            order.status = request.data['status']
            order.save()

        return Response('Success.', status=status.HTTP_200_OK)

    return Response('Fail.', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_order_item(request):
    """ Get all orders items """
    order_item = get_object_or_404(OrderItem, pk=request.query_params.get('order_id'))
    serializer = OrderItemSerializer(order_item)
    return Response(serializer.data)


@api_view(['POST'])
def order_item_create(request):
    """ Add a new orders item """
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def order_item_delete(request):
    """ Delete an orders item """
    order_item = get_object_or_404(OrderItem, pk=request.query_params.get('order_id'))
    order_item.delete()
    return Response(status=status.HTTP_200_OK)
