"""
Rotinas para acesso ao MySQL.

Banco de dados MySQL criado no container local

Seguem os dados para acesso:
Hostname: 192.168.99.100
Port: 3306
Username: my_user_name
Password: somethingSecret
Database: mysql_demo
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://my_user_name:somethingSecret@192.168.99.100:3306/mysql_demo"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#
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
