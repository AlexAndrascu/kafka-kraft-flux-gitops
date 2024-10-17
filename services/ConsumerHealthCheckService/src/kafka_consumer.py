from kafka import KafkaConsumer
import json
import os
import threading

class KafkaConsumerService:
    def __init__(self, topic, bootstrap_servers):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            security_protocol='SASL_PLAINTEXT',
            sasl_mechanism='SCRAM-SHA-256',
            sasl_plain_username=os.getenv('KAFKA_USERNAME'),
            sasl_plain_password=os.getenv('KAFKA_PASSWORD')
        )
        self.latest_message = None
        self.lock = threading.Lock()
        self._start_consumer_thread()

    def _start_consumer_thread(self):
        def consume():
            for message in self.consumer:
                with self.lock:
                    self.latest_message = message.value

        thread = threading.Thread(target=consume)
        thread.daemon = True
        thread.start()

    def get_latest_message(self):
        with self.lock:
            return self.latest_message