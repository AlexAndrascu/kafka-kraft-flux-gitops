import json
import logging
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka consumer configuration
bootstrap_servers = 'kafka-broker1:9092,kafka-broker2:9092,kafka-broker3:9092'
topic = 'health_checks_topic'

# Create Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    group_id='consumer-health-check-service'
)

def get_latest_health_check():
    latest_health_check = None
    for message in consumer:
        health_check = json.loads(message.value)
        if not latest_health_check or health_check['timestamp'] > latest_health_check['timestamp']:
            latest_health_check = health_check
    return latest_health_check

if __name__ == '__main__':
    latest_health_check = get_latest_health_check()
    if latest_health_check:
        logger.info('Latest health check:')
        logger.info(f'Service Name: {latest_health_check["service_name"]}')
        logger.info(f'Status: {latest_health_check["status"]}')
        logger.info(f'Timestamp: {latest_health_check["timestamp"]}')
    else:
        logger.info('No health check messages found')