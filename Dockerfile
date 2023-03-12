# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update package list and install required system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint command to run the main.py script
CMD ["python", "main.py"]
