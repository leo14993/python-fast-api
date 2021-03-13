from main import app
from src.bootloader.database.configuration.redis import redis_cache


@app.delete("/delete_redis", response_model=str)
def delete_redis():
    redis_cache.flush()
    return "ok"


@app.delete("/delete_key", response_model=str)
def delete_key(key: str):
    redis_cache.delete(key)
    return "ok"


@app.get("/keys_redis")
def keys_redis():
    return redis_cache.keys()