import logging
from flask import Flask, jsonify
from kafka_consumer import KafkaConsumerService

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Kafka consumer configuration
TOPIC = 'health_checks_topic'
BOOTSTRAP_SERVERS = ['kafka-h-controller-0.kafka-h-controller-headless.kafka-healthcheck.svc.cluster.local:9092']

kafka_consumer_service = KafkaConsumerService(TOPIC, BOOTSTRAP_SERVERS)

@app.route('/get_latest_health_check', methods=['GET'])
def get_latest_health_check():
    # Retrieve and print the latest health check results from the Kafka topic
    latest_health_check = kafka_consumer_service.get_latest_message()
    if latest_health_check:
        logging.info(f"Latest health check: {latest_health_check}")
        return jsonify(latest_health_check)
    else:
        return jsonify({"message": "No health check messages received yet."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)