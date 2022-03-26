import random
from mac_generator import main
from migrations.models import session, Device, Endpoint
from config import engine
from sqlalchemy import func
from http import HTTPStatus
types = ['emeter', 'zigbee', 'lora', 'gsm']
conn = engine.connect()

def append_elements():
    def get_type():
        dev_type = types[random.randint(0, 3)]
        return dev_type

    def get_id():
        dev_id = main()
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
    

devices_without_endpoint = session.query(func.count(Device.id), Device.dev_type).filter(
    Device.id.notin_(session.query(Endpoint.device_id))).group_by(Device.dev_type).all()
print(devices_without_endpoint)
