#!/bin/sh

echo "Starting plague docker"
docker run --rm -it \
    -v $(pwd)/sources:/home/plague/bin \
    -v $(pwd)/data:/home/plague/data \
    -p 8011:8000 \
    plague sh

