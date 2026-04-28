# FASTapiAnalitycs

## Docker — prod

Сборка и запуск напрямую:

- `docker build -t full-fastapi -f Dockerfile.web --target prod .`
- `docker run -p 80:80 full-fastapi`

Через compose (по умолчанию = prod):

- `docker compose up --build`
- `docker compose down`

Открыть: <http://localhost>

## Docker — dev (hot-reload)

Базовый `compose.yml` + override `compose.dev.yml`:

- `docker compose -f compose.yml -f compose.dev.yml up --build`
- `docker compose -f compose.yml -f compose.dev.yml down`

Код из `./src` монтируется в контейнер, uvicorn перезапускается на каждое
изменение. Открыть: <http://localhost:8000>


`http://0.0.0.0:8000/docs`

`http://0.0.0.0:8000`