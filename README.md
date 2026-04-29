# FASTapiAnalitycs

## Docker — dev (hot-reload)

Базовый сценарий — `compose.yml` собирает dev-стадию `Dockerfile.web`,
монтирует `./src` внутрь контейнера и запускает uvicorn с `--reload`.

- `docker compose up --build`
- `docker compose down`

Открыть:

- API: <http://localhost:8002>
- Swagger UI: <http://localhost:8002/docs>

При правке кода в `./src` uvicorn внутри контейнера сам перезапускается.
Пересборка образа нужна только при изменении `requirements.txt`,
`Dockerfile.web` или `compose.yml` — для этого можно запустить:

- `docker compose watch`

## Docker — prod (без compose)

Прод-стадия собирается напрямую и запускает gunicorn + uvicorn workers
через `./boot/start.sh`:

- `docker build -t full-fastapi:prod -f Dockerfile.web --target prod .`
- `docker run -p 80:80 -e PORT=80 -e WEB_CONCURRENCY=2 full-fastapi:prod`



- `docker compose up --watch`
- `docker compose down`
- `docker compose run app /bin/bash`
- `docker compose run app python`