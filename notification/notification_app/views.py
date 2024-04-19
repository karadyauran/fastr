import os

import requests


def send_kafka_notification(email, name):
    return requests.post(
        os.getenv('DOMAIN_LINK'),
        auth=("api", os.getenv("MAIL")),
        data={
            "from": f"Fastr <{os.getenv('MAIL_ADDRESS')}>",
            "to": f"{name} <{email}>",
            "subject": f"Hello, {name}",
            "text": 'New login',
        })
