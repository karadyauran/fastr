from django.shortcuts import get_object_or_404
from order.order_app.models.order_model import Order


def get_order_id(user_id):
    """ Retrieve order ID for a given user ID """
    cart = get_object_or_404(Order, user=user_id)
    return cart.id
