from django.core.management.base import BaseCommand
from confluent_kafka import Producer
import json


class Command(BaseCommand):
    help = 'Sends messages to Kafka'

    def handle(self, *args, **options):
        self.stdout.write("Sending message to Kafka...")
        self.kafka_producer('localhost:9092', 'auth-topic', 'example_user@example.com', 'example_user')

    def kafka_producer(self, bootstrap_servers, topic, data):
        producer = Producer({'bootstrap.servers': bootstrap_servers})
        message = json.dumps({'email': data['email'], 'first_name': data['first_name']})

        def acked(err, msg):
            if err is not None:
                self.stdout.write(f"Failed to deliver message: {err}")
            else:
                self.stdout.write(f"Message delivered to {msg.topic()} [{msg.partition()}]")

        producer.produce(topic, message.encode('utf-8'), callback=acked)
        producer.flush()
