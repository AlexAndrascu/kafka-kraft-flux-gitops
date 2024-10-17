import logging
from flask import Flask, jsonify
from kafka import KafkaConsumer
import json
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Kafka consumer configuration
TOPIC = 'health_checks_topic'
BOOTSTRAP_SERVERS = ['kafka-h-controller-0.kafka-h-controller-headless.kafka-healthcheck.svc.cluster.local:9092']

kafka_consumer_service = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    group_id='health_check_service_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='SCRAM-SHA-256',
    sasl_plain_username=os.getenv('KAFKA_USERNAME'),
    sasl_plain_password=os.getenv('KAFKA_PASSWORD')
)

@app.route('/check_health', methods=['GET'])
def check_health():
    health_statuses = []
    for message in kafka_consumer_service:
        logging.info(f"Service: {message.value['service_name']}, Status: {message.value['status']}, Timestamp: {message.value['timestamp']}")
        health_statuses.append(message.value)
    return jsonify(health_statuses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)