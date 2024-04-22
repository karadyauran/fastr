from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from order.order_app.models.cart_item_model import CartItem
from order.order_app.serializers import OrderSerializer
from order.order_app.serializers.order_item_serializer import OrderItemSerializer
from order.order_app.utils import get_user_id, get_cart_id
from order.order_app.views.order_view import calculate_total_price, create


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add_all_from_cart(request):
    user_id = get_user_id(request=request)
    cart_items = CartItem.objects.filter(cart=get_cart_id(user_id=user_id))

    if not cart_items:
        return Response({'error': 'Cart has no items'}, status=status.HTTP_400_BAD_REQUEST)

    token_key = request.headers.get('Authorization').split()[1]
    token = get_object_or_404(Token, key=token_key)

    order = create(token)  # Create order
    order_id = order.id

    for cart_item in cart_items:
        data = {
            'order': order_id,
            'product': cart_item.product.id,
            'quantity': cart_item.quantity,
        }

        serializer = OrderItemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

    calculate_total_price(order_id)

    return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
