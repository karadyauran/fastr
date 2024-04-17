from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from cart.cart_app.models.cart_model import Cart
from cart.cart_app.models.cart_item_model import CartItem
from cart.cart_app.serializers.cart_serializer import CartSerializer
from cart.cart_app.serializers.cart_item_serializer import CartItemSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get_user_id(request=None, token=None):
    if request:
        token_key = request.headers.get('Authorization').split()[1]
        token = Token.objects.get(key=token_key)
    elif not token:
        raise ValueError("Token is not provided")
    return token.user.id


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def create_cart(token):
    user_id = get_user_id(token=token)
    data = {
        'user_id': user_id,
    }
    serializer = CartSerializer(data=data)

    if serializer.is_valid():
        serializer.create(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get(request):
    """ Get cart items """
    user_id = get_user_id(request)
    cart = get_object_or_404(Cart, id=user_id)
    serializer = CartSerializer(cart)

    return Response(serializer.data, status=status.HTTP_200_OK)


def calculate_total_price(user_id):
    """ Calculate total price of cart items """
    cart_id = user_id

    cart_items = CartItem.objects.filter(cart_id=cart_id)
    serializer = CartItemSerializer(cart_items, many=True)

    total_price = 0

    for cart_item in serializer.data:
        cart_item = CartItem.objects.get(id=cart_item.get('id'))
        total_price = cart_item.product_id.price * cart_item.quantity

    cart = get_object_or_404(Cart, id=cart_id)
    cart.set_total_price(total=total_price)
    cart.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
