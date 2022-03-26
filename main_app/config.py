from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("postgresql://postgres:1234@localhost/devices", echo=True)
session_local = sessionmaker(autocommit=True, bind=engine)
engine.connect()


def get_db():
    db = session_local()
    try:
        yield db
    except:
        db.close()
