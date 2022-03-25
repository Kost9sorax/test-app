import random
from mac_generator import main
from sql_alchemy import session, Device, Endpoint
types = ['emeter', 'zigbee', 'lora', 'gsm']


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
