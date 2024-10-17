import logging
import requests
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# HealthCheckService configuration
HEALTH_CHECK_SERVICE_URL = 'http://health-check-service.kafka-healthcheck:80/check_health'

@app.route('/get_latest_health_check', methods=['GET'])
def get_latest_health_check():
    logging.info("Received request for latest health check")
    try:
        logging.info(f"Fetching health check data from {HEALTH_CHECK_SERVICE_URL}")
        response = requests.get(HEALTH_CHECK_SERVICE_URL)
        logging.info(f"Response status code: {response.status_code}")
        response.raise_for_status()
        health_checks = response.json()
        logging.info(f"Health checks received: {health_checks}")
        if health_checks:
            latest_health_check = health_checks[-1]  # Get the latest health check
            logging.info(f"Latest health check: {latest_health_check}")
            return jsonify(latest_health_check)
        else:
            logging.info("No health check messages received yet.")
            return jsonify({"message": "No health check messages received yet."}), 404
    except requests.RequestException as e:
        logging.error(f"Error fetching health check data: {e}")
        return jsonify({"message": "Error fetching health check data."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)