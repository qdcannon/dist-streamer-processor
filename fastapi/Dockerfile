# Use an official base image with build tools
FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install python and dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev build-essential libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install fastapi httpx

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Default command runs the app
WORKDIR /app/src/fastapi
CMD ["python3 filehandler.py"]
