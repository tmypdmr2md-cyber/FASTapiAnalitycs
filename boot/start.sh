#!/bin/bash
set -e

PORT="${PORT:-80}"
WORKERS="${WEB_CONCURRENCY:-2}"

exec gunicorn src.main:app \
    --workers "$WORKERS" \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind "0.0.0.0:$PORT" \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
