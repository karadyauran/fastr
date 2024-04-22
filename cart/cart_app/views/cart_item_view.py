from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.cart_app.models.cart_item_model import CartItem
from cart.cart_app.models.cart_model import Cart
from cart.cart_app.models.product_model import Product
from cart.cart_app.serializers.cart_item_serializer import CartItemSerializer
from cart.cart_app.utils.utils import get_user_id, get_cart_id, check_product
from cart.cart_app.views.cart_view import calculate_total_price


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add(request):
    """ Add cart item """
    user_id = get_user_id(request=request)
    product_id = request.query_params.get('product_id')
    if not product_id or not check_product(product_id):
        return Response({'error': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    quantity = request.query_params.get('quantity', 1)

    cart_instance = get_object_or_404(Cart, pk=get_cart_id(user_id))
    product_instance = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart_instance, product=product_instance,
                                                        defaults={'quantity': quantity})

    if not created and quantity:
        cart_item.quantity += int(quantity)
        cart_item.save()

    calculate_total_price(get_cart_id(user_id))
    return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def edit_cart_item_quantity(request):
    """ Edit cart item quantity """
    user_id = get_user_id(request=request)
    cart_id = get_cart_id(user_id)
    cart_item = get_object_or_404(CartItem, pk=request.query_params.get('cart_item_id'))
    cart_item.quantity = request.query_params.get('quantity', cart_item.quantity)
    cart_item.save()
    calculate_total_price(cart_id)
    return Response('CartItem quantity updated', status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def remove(request):
    """ Remove cart item """
    user_id = get_user_id(request=request)
    cart_id = get_cart_id(user_id)
    cart_item = get_object_or_404(CartItem, pk=request.query_params.get('cart_item_id'))
    cart_item.delete()
    calculate_total_price(cart_id)
    return Response('Cart item deleted', status=status.HTTP_200_OK)
