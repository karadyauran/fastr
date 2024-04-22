from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from order.order_app.models.cart_model import Cart
from order.order_app.models.order_model import Order
from order.order_app.models.product_model import Product


def get_cart_id(user_id):
    """ Retrieve cart ID for a given user ID """
    cart = get_object_or_404(Cart, user=user_id)
    return cart.id


def get_order_id(user_id):
    """ Retrieve order ID for a given user ID """
    cart = get_object_or_404(Order, user=user_id)
    return cart.id


def get_user_id(request=None, token=None):
    """ Extract user ID from request token """
    if not token:
        token_key = request.headers.get('Authorization').split()[1]
        token = get_object_or_404(Token, key=token_key)
    return token.user.id


def check_product(product_id):
    """ Check if a product exists by ID """
    return Product.objects.filter(id=product_id).exists()
