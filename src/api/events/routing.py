from fastapi import APIRouter
# говорим в каком формате мы хотим возвращать данные
from .schema import EventSchema

router = APIRouter() 


@router.get("/")
def read_events():
    return {
        "items" : "[1, 2, 3]"
    }

@router.get("/{event_id}")
def get_events(event_id: int) -> EventSchema:
    return {"id": event_id}