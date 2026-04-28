# Точка входа FastAPI-приложения.
# Запуск локально (без Docker):
#   uvicorn src.main:app --reload
# В Docker этим занимается compose.yml (dev) или ./boot/start.sh (prod).

from fastapi import FastAPI

# Объект `app` — то, что ищут uvicorn/gunicorn по пути `src.main:app`.
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    # item_id приходит из пути, q — опциональный query-параметр (?q=...).
    return {"item_id": item_id, "q": q}
