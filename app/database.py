from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative
from settings import DB_URL

# Create the database engine
engine = create_engine(
    DB_URL, connect_args={"check_same_thread": False}  # SQLite-specific configuration
)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
@as_declarative()
class Base:
    pass

# Dependency for FastAPI routes to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
