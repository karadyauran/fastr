import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe

from django.conf import settings

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


@api_view(['POST'])
def payment(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': request.data['name'],
                },
                'unit_amount': request.data['amount'],
            },
            'quantity': request.data['quantity'],
        }],
        mode='payment',
    )

    return Response('Success', status=status.HTTP_200_OK)


@api_view(['POST'])
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META[os.getenv('HTTP_STRIPE_SIGNATURE')]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except stripe.error.SignatureVerificationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

    return Response(status=status.HTTP_200_OK)
