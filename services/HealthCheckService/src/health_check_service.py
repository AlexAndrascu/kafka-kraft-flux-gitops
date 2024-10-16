import time
import logging
from kafka import KafkaConsumer
import json

class HealthCheckService:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'health_checks_topic',
            bootstrap_servers='kafka-h-controller-0.kafka-h-controller-headless.kafka-healthcheck.svc.cluster.local:9092',
            group_id='health_check_service_group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
    
    def check_health(self):
        while True:
            for message in self.consumer:
                health_check = message.value
                service_name = health_check.get('service_name')
                status = health_check.get('status')
                timestamp = health_check.get('timestamp')
                
                logging.info(f"Health check result for {service_name}: {status} at {timestamp}")
                
            time.sleep(60)  # Perform health checks every 60 seconds

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    health_check_service = HealthCheckService()
    health_check_service.check_health()