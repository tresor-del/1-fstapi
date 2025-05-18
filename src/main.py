from typing import Union

from fastapi import FastAPI
from api.events import router as event_router

app = FastAPI()
app.include_router(event_router, prefix='/api/events')


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/healthz")
async def read_api_health():
    return {'status': 'ok'}