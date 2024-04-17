from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.cart_app.models.cart_item_model import CartItem
from cart.cart_app.serializers.cart_item_serializer import CartItemSerializer

from product.product_app.models.product_model import Product

from cart.cart_app.views.cart_view import calculate_total_price


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def get_user_id(request) -> int:
    """ Check if a user is a staff user. """
    token_key = request.headers.get('Authorization').split()[1]
    token = Token.objects.get(key=token_key)
    user = token.user

    return user.id


def check_product(product_id: int) -> bool:
    """ Check if cart item exists """
    return Product.objects.filter(id=product_id).exists()


@api_view(['POST'])
def add(request):
    """ Add cart item """
    user_id = get_user_id(request)
    product_id = request.data.get('product_id')
    if not product_id or not check_product(product_id):
        return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    quantity = request.data.get('quantity', 1)
    cart_item, created = CartItem.objects.get_or_create(cart_id=user_id, product_id=product_id,
                                                        defaults={'quantity': quantity})

    if not created and quantity:
        cart_item.quantity += int(quantity)
        cart_item.save()

    calculate_total_price(user_id)

    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def edit_cart_item_quantity(request):
    """ Edit cart item quantity """
    cart = get_object_or_404(CartItem, pk=request.query_params.get('cart_id'))
    cart.quantity = request.data.get('quantity', cart.quantity)
    cart.save()

    calculate_total_price(request)

    return Response('CartItem quantity updated', status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove(request):
    """ Remove cart item """
    cart_item = get_object_or_404(CartItem, pk=request.query_params.get('cart_id'))
    cart_item.delete()

    calculate_total_price(request)

    return Response('Cart item deleted', status=status.HTTP_200_OK)
