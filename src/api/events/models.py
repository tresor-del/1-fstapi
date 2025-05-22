from typing import List, Optional
from sqlmodel import SQLModel, Field



class EventModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page: Optional[str] = ''
    description: Optional[str] = ''

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default='default description')

class EventUpdateSchema(SQLModel):
    description: str

class EventListSchema(SQLModel):
    results: List[EventModel]