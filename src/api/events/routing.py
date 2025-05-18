import os

from fastapi import APIRouter, Depends
from api.db.session import get_session
from sqlmodel import Session
from .models import (
    EventModel, 
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema,
) 

router = APIRouter()
from api.db.config import DATABASE_URL

@router.get('/')
def read_events() -> EventListSchema:
    print(os.environ.get('DATABASE_URL'), DATABASE_URL)
    return {
        'results': [
            {'id': 1}, {'id': 2}, {'id': 3}
        ]
    }

@router.post('/', response_model=EventModel)
def create_events(
    payload:EventCreateSchema,
    session: Session = Depends(get_session)):
    print(payload)
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get('/{event_id}')
def get_events(event_id: int) -> EventModel:
    return {'id': event_id}

@router.put('/{event_id}')
def update_events(event_id:int, payload:EventUpdateSchema) -> EventModel:
    print(payload)
    data = payload.model_dump()
    return {'id': event_id, **data}


# @router.delete('/{event_id}')
# def delete_events(event_id: int) -> EventModel:
#     return {'id': event_id}