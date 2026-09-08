import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ganti 'postgres' dan 'passwordku' sesuai dengan username dan password PostgreSQL kamu
DATABASE_URL = "postgresql://postgres:Sorryboy28@localhost:5432/bug_tracker"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Fungsi untuk mendapatkan sesi database di setiap request API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()