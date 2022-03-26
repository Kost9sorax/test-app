from main import app, is_anagrams, redis_client


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
