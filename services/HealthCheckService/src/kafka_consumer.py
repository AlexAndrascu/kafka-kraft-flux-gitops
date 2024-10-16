from kafka import KafkaConsumer

class KafkaConsumerService:
    def __init__(self, topic):
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers='localhost:9092',
            group_id='health_check_group'
        )

    def consume_messages(self):
        for message in self.consumer:
            # Pass the message to the HealthCheckService for processing
            HealthCheckService.process_message(message.value)

if __name__ == "__main__":
    # Create an instance of KafkaConsumerService and start consuming messages
    consumer_service = KafkaConsumerService('health_checks_topic')
    consumer_service.consume_messages()