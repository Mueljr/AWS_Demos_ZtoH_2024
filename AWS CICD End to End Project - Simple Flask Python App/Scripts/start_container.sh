#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
echo (docker pull username/containername)

# Run the Docker image as a container
echo (docker run -d -p portno:portno username/containername)
