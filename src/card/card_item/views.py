from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CartItem
from .serializer import CartSerializer

from django.shortcuts import get_object_or_404
from rest_framework import status

import requests


def get_user_id(request):
    """ Get user id from token """
    token = request.headers.get('Authorization')

    if not token:
        return Response({'error': 'Token is missing'}, status=400)

    user_response = requests.get('http://127.0.0.1:8001/api/v3/user/get_user_id', headers={'Authorization': token})

    if user_response.status_code == 200:
        return user_response.json()['id']
    else:
        return -1


@api_view(['POST'])
def add(request):
    """ Add a card item """
    user_id = get_user_id(request)

    if user_id == -1:
        return Response({'error': 'Token is missing'}, status=400)

    product_id = request.data['product_id']
    product_response = requests.get(f'http://127.0.0.1:8000/api/v3/product/exists?id={product_id}')

    if product_response.status_code == 200:
        product_exists = product_response.json()['exists']

        if not product_exists:
            return Response({'error': 'Product does not exist'}, status=400)
    else:
        return Response({'error': product_response.status_code}, status=400)

    data = {
        'user_id': user_id,
        'product_id': product_id,
        'quantity': request.data['quantity'] if 'quantity' in request.data else 1,
    }

    serializer = CartSerializer(data=data)

    if serializer.is_valid():
        serializer.create(data)

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get(request):
    """ Get a cart items """
    user_id = get_user_id(request)

    if user_id == -1:
        return Response({'error': 'Token is missing'}, status=400)

    cart = CartItem.objects.filter(user_id=user_id)
    serializer = CartSerializer(cart, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove(request):
    """ Remove a cart item """
    cart_item = get_object_or_404(CartItem, pk=request.data['id'])
    cart_item.delete()
    return Response('Card item deleted', status=status.HTTP_200_OK)
