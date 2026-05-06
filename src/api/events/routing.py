from uuid import UUID, uuid4

from fastapi import APIRouter

# говорим в каком формате мы хотим возвращать данные
from .schema import EventListSchema, EventSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()

"""
api methods:
GET    /api/events/             - возвращает список событий
POST   /api/events/             - создает новое событие
GET    /api/events/{event_id}   - возвращает событие по id
PUT    /api/events/{event_id}   - обновляет описание события по id
DELETE /api/events/{event_id}   - удаляет событие по id
"""


# GET /api/events/ - возвращает список событий
@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [
            {"id": uuid4()},
            {"id": uuid4()},
            {"id": uuid4()},
        ],
        "count": 3,
    }


# POST /api/events/ - создает новое событие
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    data = payload.model_dump()
    return {
        "id": uuid4(),
        **data,
    }


# GET /api/events/{event_id} - возвращает событие по id
@router.get("/{event_id}")
def get_events(event_id: UUID) -> EventSchema:
    return {"id": event_id}


# PUT /api/events/{event_id} - обновляет описание события по id
@router.put("/{event_id}")
def update_event(event_id: UUID, payload: EventUpdateSchema) -> EventSchema:
    return {
        "id": event_id,
        "path": payload.path,
        "description": payload.description,
    }


# DELETE /api/events/{event_id} - удаляет событие по id
@router.delete("/{event_id}")
def delete_event(event_id: UUID):
    pass
