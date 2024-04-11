from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import CartItem
from .serializer import CartSerializer


def get_user_id(token):
    """ Get user id from token """
    if not token:
        return None, 'Token is missing'

    user_response = requests.get('http://127.0.0.1:8001/api/v3/user/get_user_id', headers={'Authorization': token})
    if user_response.status_code == 200:
        return user_response.json()['id'], None
    else:
        return None, 'User not found'


def check_product(product_id):
    """ Check if cart item exists """
    product_response = requests.get(f'http://127.0.0.1:8000/api/v3/product/exists?id={product_id}')
    if product_response.status_code == 200 and product_response.json()['exists']:
        return True
    return False


@api_view(['POST'])
def add(request):
    """ Add cart item """
    token = request.headers.get('Authorization')
    user_id, error = get_user_id(token)
    if not user_id:
        return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

    product_id = request.data.get('product_id')
    if not product_id or not check_product(product_id):
        return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    quantity = request.data.get('quantity', 1)
    cart_item, created = CartItem.objects.get_or_create(user_id=user_id, product_id=product_id,
                                                        defaults={'quantity': quantity})

    if not created and quantity:
        cart_item.quantity += int(quantity)
        cart_item.save()

    serializer = CartSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def edit_cart_item_quantity(request, cart_id):
    """ Edit cart item quantity """
    cart = get_object_or_404(CartItem, pk=cart_id)
    cart.quantity = request.data.get('quantity', cart.quantity)
    cart.save()
    return Response('CartItem quantity updated', status=status.HTTP_200_OK)


@api_view(['GET'])
def get(request):
    """ Get cart items """
    token = request.headers.get('Authorization')
    user_id, error = get_user_id(token)
    if not user_id:
        return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)

    cart_items = CartItem.objects.filter(user_id=user_id)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove(request, cart_id):
    """ Remove cart item """
    cart_item = get_object_or_404(CartItem, pk=cart_id)
    cart_item.delete()
    return Response('Cart item deleted', status=status.HTTP_200_OK)
