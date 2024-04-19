from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaError
import json

from notification.notification_app.views import send_kafka_notification


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.kafka_consumer('localhost:9092', 'auth-topic')

    def kafka_consumer(self, bootstrap_servers, topic):
        settings = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': 'message-service-group',
            'auto.offset.reset': 'earliest'
        }
        consumer = Consumer(settings)
        consumer.subscribe([topic])

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        self.stdout.write(f"Consumer error: {msg.error()}")
                        break

                data = json.loads(msg.value().decode('utf-8'))
                send_kafka_notification(email=data['email'], name=data['first_name'])
        finally:
            consumer.close()
