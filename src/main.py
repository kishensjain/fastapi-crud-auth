from fastapi import FastAPI
from .database import engine
from . import models
from .routers import users

models.Base.metadata.create_all(bind=engine) #It tells SQLAlchemy: Create tables in the database if they do not exist.

app = FastAPI(title="FastAPI CRUD Auth")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API is running"}