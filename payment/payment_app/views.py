import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe


from payment.config.settings import STRIPE_TEST_SECRET_KEY, STRIPE_WEBHOOK_SECRET
from payment.payment_app.models import OrderItem

stripe.api_key = STRIPE_TEST_SECRET_KEY


@api_view(['POST'])
def payment(request):
    try:
        order_items = OrderItem.objects.filter(order_id=request.data['order_id'])

        line_items = [{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': order_item.product.name,
                },
                'unit_amount': int(float(order_item.product.price) * 100),
            },
            'quantity': order_item.quantity,
        } for order_item in order_items]

        if not line_items:
            return Response({'error': 'No items in the order'}, status=status.HTTP_404_NOT_FOUND)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url="https://google.com",
            cancel_url="https://python.org",
        )

        return Response({'url': session.url}, status=status.HTTP_303_SEE_OTHER)
    except stripe.error.StripeError as e:
        return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META[os.getenv('HTTP_STRIPE_SIGNATURE')]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except stripe.error.SignatureVerificationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

    return Response(status=status.HTTP_200_OK)
