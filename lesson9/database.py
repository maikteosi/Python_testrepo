from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = 'postgres'
DB_PASSWORD = '121'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'QA1'

DATABASE_URL = (f"postgresql:"
                f"//{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Создаем engine
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
