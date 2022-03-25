from sqlalchemy import Integer, String, Index, BIGINT
from sqlalchemy.sql.schema import Column
from config import Base, engine
from sqlalchemy.orm import sessionmaker, relationship

Session = sessionmaker()
session = Session(bind=engine)


class Device(Base):
    __tablename__ = 'Devices'
    id = Column(Integer(), primary_key=True)
    dev_id = Column(String(200), nullable=False)
    dev_type = Column(String(120), nullable=False)

    def __init__(self, dev_id, dev_type):
        self.dev_id = dev_id
        self.dev_type = dev_type


class Endpoint(Base):
    __tablename__ = 'Endpoints'
    id = Column(BIGINT, primary_key=True)
    device_id = Column(Integer)
    comment = Column(String)

    def __init__(self, device_id, comment):
        self.device_id = device_id
        self.comment = comment


device_index = Index('device_index', Device.dev_id, Device.dev_type)

if __name__ == '__main__':
    device_index.create(bind=engine)

session.commit()
