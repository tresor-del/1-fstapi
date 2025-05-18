from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI
from api.db.session import init_db
from api.events import router as event_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app start up
    init_db()
    yield
    # clean up


app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix='/api/events')


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/healthz")
async def read_api_health():
    return {'status': 'ok'}