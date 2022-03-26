import random
from migrartions.models import session, Device, Endpoint
from main_app.config import engine
from sqlalchemy import func
from randmac import RandMac

types = ['emeter', 'zigbee', 'lora', 'gsm']
conn = engine.connect()


def append_elements():
    def get_type():
        dev_type = types[random.randint(0, 3)]
        return dev_type

    def get_id():
        dev_id = RandMac()
        return str(dev_id)

    for i in range(0, 10):
        session.add(Device(get_id(), get_type()))
        session.commit()

    devices = session.query(Device)

    ids = []
    for device in devices:
        ids.append(device.id)

    for i in range(5):
        session.add(Endpoint(ids[i], 'some comment'))
    session.commit()

    
def dev_without_endpoint():
    rows = session.query(func.count(Device.id), Device.dev_type).filter(
        Device.id.notin_(session.query(Endpoint.device_id))).group_by(Device.dev_type).all()
    new_rows = {}
    for row in rows:
        new_rows[row[1]] = row[0]
    return new_rows
