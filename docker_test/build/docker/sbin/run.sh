#!/bin/sh

echo "Starting plague docker"
python3 "$PLAGUE_BIN/messenger/manage.py" runserver 0.0.0.0:8000
