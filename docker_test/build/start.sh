#!/bin/sh

echo "Building plague docker"
docker build -f ./build/docker/Dockerfile -t plague ./build/docker/

echo "Starting plague docker"
docker run --rm -d \
    -v $(pwd)/sources:/home/plague/bin \
    -v $(pwd)/data:/home/plague/data \
    -p 8011:8000 \
    plague

