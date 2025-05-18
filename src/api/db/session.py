import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print('creating database')
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session