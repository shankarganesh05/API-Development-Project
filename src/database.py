from sqlmodel import Session,create_engine
from .config import settings


DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

engine = create_engine(DATABASE_URL)
def get_session():
    with Session(engine) as session:
        yield session

