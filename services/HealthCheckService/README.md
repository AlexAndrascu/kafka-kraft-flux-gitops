# HealthCheckService

This project contains a Python service named HealthCheckService that periodically performs health checks on various microservices in the system.

## Project Structure

The project has the following files:

- `src/__init__.py`: This file is an empty file that marks the `src` directory as a Python package.

- `src/health_check_service.py`: This file contains the implementation of the `HealthCheckService` class. It periodically performs health checks on various microservices by consuming messages from the Kafka topic `health_checks_topic`. It has a REST API endpoint `/check_health` that retrieves the health status of different microservices and prints the results along with some text to the logs.

- `src/kafka_consumer.py`: This file contains the implementation of the Kafka consumer that consumes messages from the `health_checks_topic` and passes them to the `HealthCheckService` for processing.

- `requirements.txt`: This file lists the dependencies required for the project. It specifies the Python packages and their versions that need to be installed.

- `Dockerfile`: This file is used to build a Docker image for the project. It specifies the base image, copies the necessary files, and sets up the environment for running the Python service.

## Setup and Usage

To set up and run the HealthCheckService, follow these steps:

1. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

2. Build the Docker image by running the following command:
   ```
   docker build -t healthcheckservice .
   ```

3. Run the Docker container by running the following command:
   ```
   docker run -d --name healthcheckservice-container healthcheckservice
   ```

4. Access the HealthCheckService API by sending HTTP requests to `http://localhost:5000/check_health`.

## Contributing

Contributions to the HealthCheckService project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

Please note that the specific implementation details of the classes and functions inside the Python files are not provided in the project tree structure.