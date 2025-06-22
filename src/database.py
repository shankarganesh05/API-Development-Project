from sqlmodel import Session,create_engine


DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/fastapi"

engine = create_engine(DATABASE_URL)
def get_session():
    with Session(engine) as session:
        yield session

