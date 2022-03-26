from main_app.storage import append_elements
from fastapi import FastAPI
import redis
from fastapi import Response

redis_client = redis.Redis(host='localhost', port=6379, db=0)
app = FastAPI()


@app.get('/{str_1}/{str_2}')
def get_anagrams(str_1, str_2):
    if is_anagrams(str_1, str_2):
        if redis_client.get("counter"):
            redis_client.set("counter", int(redis_client.get("counter")) + 1)
        else:
            redis_client.set("counter", 1)
        return {"is anagrams": True, "counter": redis_client.get("counter")}
    else:
        return {"is anagrams": False}


@app.get('/add')
def add_elements():
    append_elements()
    return Response(status_code=201)


def is_anagrams(str_1, str_2):
    len_str_1 = len(str_1)
    len_str_2 = len(str_2)

    if len_str_1 != len_str_2:
        return False

    sort_str_1 = sorted(str_1.lower())
    sort_str_2 = sorted(str_2.lower())

    for i in range(0, len_str_1):
        if sort_str_1[i] != sort_str_2[i]:
            return False
    return True
