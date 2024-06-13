from fastapi import FastAPI
from .database import engine, Base
from .routers import configuration

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configuration.router, prefix="/configurations", tags=["configurations"])
