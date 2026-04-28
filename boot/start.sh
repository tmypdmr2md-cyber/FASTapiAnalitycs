#!/bin/bash
# start.sh

exec gunicorn src.main:app \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:80 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -