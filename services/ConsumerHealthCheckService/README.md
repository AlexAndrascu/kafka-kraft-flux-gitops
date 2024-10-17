# ConsumerHealthCheckService

This project contains a Python service named ConsumerHealthCheckService that consumes health check messages from the `health_checks_topic` in Kafka. It provides a REST API endpoint `/get_latest_health_check` to retrieve and print the latest health check results from the Kafka topic.

## Project Structure

```
ConsumerHealthCheckService
├── src
│   ├── __init__.py
│   ├── consumer_health_check_service.py
│   └── kafka_consumer.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
└── README.md
```

- `src/__init__.py`: This file is an empty file that marks the `src` directory as a Python package.

- `src/consumer_health_check_service.py`: This file contains the implementation of the ConsumerHealthCheckService. It includes a REST API endpoint `/get_latest_health_check` that retrieves and prints the latest health check results from the Kafka topic.

- `src/kafka_consumer.py`: This file contains the implementation of the Kafka consumer. It handles the consumption of health check messages from the `health_checks_topic` in Kafka.

- `requirements.txt`: This file lists the dependencies required for the project. Make sure to install these dependencies before running the service.

- `Dockerfile`: This file is used to build a Docker image for the ConsumerHealthCheckService. It includes instructions to install the necessary dependencies, copy the source code, and configure the container.

- `deployment.yaml`: This file is a Kubernetes deployment configuration for deploying the ConsumerHealthCheckService on the Kubernetes cluster. It includes specifications for the container image, environment variables, and any other necessary configurations.

## Setup and Usage

1. Install the dependencies listed in `requirements.txt` by running the following command:

   ```
   pip install -r requirements.txt
   ```

2. Build the Docker image using the provided `Dockerfile`:

   ```
   docker build -t consumer-health-check-service .
   ```

3. Deploy the service on your Kubernetes cluster using the `deployment.yaml` file:

   ```
   kubectl apply -f deployment.yaml
   ```

4. Once deployed, you can access the service's REST API endpoint at `/get_latest_health_check` to retrieve and print the latest health check results from the Kafka topic.

Please note that you may need to configure the Kafka bootstrap server addresses and other relevant configurations in the source code and deployment file based on your specific setup.

For more information and detailed instructions, refer to the documentation or consult the project's codebase.
```

Please make sure to update the documentation with any additional information or specific instructions relevant to your project.