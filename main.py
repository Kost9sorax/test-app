from fastapi import FastAPI
import psycopg2
from config import host, user, password, db_name
import redis

# redis_client = redis.Redis(host='localhost', port=6379, db=0)
# app = FastAPI()
#
#
# def is_anagrams(str_1, str_2):
#     len_str_1 = len(str_1)
#     len_str_2 = len(str_2)
#
#     if len_str_1 != len_str_2:
#         return False
#
#     sort_str_1 = sorted(str_1.lower())
#     sort_str_2 = sorted(str_2.lower())
#
#     for i in range(0, len_str_1):
#         if sort_str_1[i] != sort_str_2[i]:
#             return False
#     return True
#
#
# @app.get('/{str_1}/{str_2}')
# def get_anagrams(str_1, str_2):
#     if is_anagrams(str_1, str_2):
#         if redis_client.get("counter"):
#             redis_client.set("counter", int(redis_client.get("counter")) + 1)
#         else:
#             redis_client.set("counter", 1)
#         return {"is anagrams": True, "counter": redis_client.get("counter")}
#     else:
#         return {"is anagrams": False}
#
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE devices(
            id bigserial not null constraint devices_pk primary key,
            dev_id varchar(200) not null,
            dev_type varchar(120) not null
            );
            alter table devices
                owner to postgres;

            create index devices_dev_id_dev_type_index
                on devices (dev_id, dev_type);

            create table endpoints
            (
                id        bigserial not null
                    constraint endpoints_pk
                        primary key,
                device_id integer
                    constraint endpoints_devices_id_fk
                        references devices
                        on update cascade on delete cascade,
                comment   text
            );

            alter table endpoints
                owner to postgres;
            '''
        )

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print('{[INFO] PostgreSQL connection closed')
