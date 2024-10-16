# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY src/ .

# Set the entrypoint command to run the health_check_service.py file
CMD ["python", "health_check_service.py"]