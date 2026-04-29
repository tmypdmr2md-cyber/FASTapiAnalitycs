
from fastapi import FastAPI

from .api.events import router as events_router

app = FastAPI()

app.include_router(events_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    # item_id приходит из пути, q — опциональный query-параметр (?q=...).
    return {"item_id": item_id, "q": q}

@app.get("/healthz")
def api_health():
    # /healthz — стандартное соглашение Kubernetes для liveness-probe.
    return {"status": "ok"}