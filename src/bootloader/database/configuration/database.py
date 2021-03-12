
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

from sqlalchemy.orm import sessionmaker

env = ".env"
dotenv_path = os.path.join('', env)
load_dotenv(dotenv_path)


SQLALCHEMY_DATABASE_URL = f"{os.getenv('DATABASE_ENGINE')}://{os.getenv('DATABASE_USER')}:" \
                          f"{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:" \
                          f"{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base: DeclarativeMeta = declarative_base()

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
