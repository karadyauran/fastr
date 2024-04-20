from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, F

from cart.cart_app.models.cart_model import Cart
from cart.cart_app.models.cart_item_model import CartItem
from cart.cart_app.serializers.cart_serializer import CartSerializer
from cart.cart_app.serializers.cart_item_serializer import CartItemSerializer
from cart.cart_app.utils.utils import get_user_id, get_cart_id


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get(request):
    """ Get cart items """
    user_id = get_user_id(request=request)
    cart_id = get_cart_id(user_id)
    cart = get_object_or_404(Cart, id=cart_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_cart(request):
    user_id = get_user_id(token=request.data.get('token'))
    serializer = CartSerializer(data={
        'user': user_id,
    })

    if serializer.is_valid():
        serializer.save()


def calculate_total_price(cart_id):
    """ Calculate total price of cart items """
    cart_items = CartItem.objects.filter(cart=cart_id)
    total_price = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0
    cart = get_object_or_404(Cart, id=cart_id)
    cart.set_total_price(total=total_price)
    cart.save()
    cart_items = cart_items.select_related('product')
    return Response(CartItemSerializer(cart_items, many=True).data, status=status.HTTP_200_OK)
