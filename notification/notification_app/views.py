import os
from datetime import time

import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def send_notification(request):
    if request.user.is_staff:
        requests.post(
            os.getenv('DOMAIN_LINK'),
            auth=("api", os.getenv("MAIL")),
            data={
                "from": f"Fastr <{os.getenv('MAIL_ADDRESS')}>",
                "to": f"{request.data.get('name')} <{request.data.get('email')}>",
                "subject": f"Hello, {request.data.get('name')}",
                "text": request.data.get("text"),
            })

        return Response('Message sent', status=status.HTTP_200_OK)


def send_kafka_notification(email, name):
    print(email, name)
    # return requests.post(
    #     os.getenv('DOMAIN_LINK'),
    #     auth=("api", os.getenv("MAIL")),
    #     data={
    #         "from": f"Fastr <{os.getenv('MAIL_ADDRESS')}>",
    #         "to": f"{name} <{email}>",
    #         "subject": f"Hello, {name}",
    #         "text": 'New login',
    #     })
