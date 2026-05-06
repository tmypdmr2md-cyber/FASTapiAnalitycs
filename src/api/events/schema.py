from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


"""
id 
path 
description
"""
class EventSchema(BaseModel):
    id: UUID
    path: Optional[str] = "" 
    description: Optional[str] = ""

    

class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int = 0

class EventCreateSchema(BaseModel):
    path: str
    description: str = ""

class EventUpdateSchema(BaseModel):
    path: str = ""
    description: str = ""

