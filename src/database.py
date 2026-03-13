from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL.startswith("postgresql://"): #type: ignore
    DATABASE_URL = DATABASE_URL.replace( #type: ignore
        "postgresql://",
        "postgresql+psycopg2://",
        1
    )

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL) 

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()

# FastAPI will automatically inject a database session into routes.
def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()