#!/bin/bash
# start.sh — entrypoint для prod-стадии Dockerfile.web.
# В dev-режиме НЕ используется: compose.yml переопределяет CMD на uvicorn --reload.

# -e: упасть при первой же ошибке любой команды (иначе контейнер
# может «успешно» стартовать с битой конфигурацией).
set -e

# Параметры берём из env, чтобы менять поведение через compose
# или `docker run -e ...` без пересборки образа.
PORT="${PORT:-80}"                 # на каком порту слушать внутри контейнера
WORKERS="${WEB_CONCURRENCY:-2}"    # сколько процессов-воркеров поднять

# exec заменяет shell-процесс gunicorn'ом → gunicorn становится PID 1.
# Это важно, чтобы он напрямую получал SIGTERM от Docker и корректно
# завершал воркеры (graceful shutdown), а не был зомби под bash.
#
# UvicornWorker превращает gunicorn (WSGI) в ASGI-совместимый — без него
# FastAPI в gunicorn не запустится.
exec gunicorn src.main:app \
    --workers "$WORKERS" \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind "0.0.0.0:$PORT" \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
