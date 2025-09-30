# Use an official base image with build tools
FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install build essentials, cmake, and OpenCV development packages
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Create build directory and build
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    make

# Default command runs the app
WORKDIR /app/build
CMD ["./MyImageCVApp"]
