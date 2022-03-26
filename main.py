from main_app.storage import append_elements, dev_without_endpoint
from fastapi import FastAPI
import redis
from fastapi import Response
from main_app.checking_anagrams import is_anagrams

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


@app.get('/get_rows')
def get_rows():
    return {'rows': dev_without_endpoint()}

