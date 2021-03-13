import os
import pickle
import redis
from dotenv import load_dotenv

env = ".env"
dotenv_path = os.path.join('', env)
load_dotenv(dotenv_path)

class RedisCacheService:

    def __init__(self, host, port, db, password):
        self.cache = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            password=password
        )

    def set(self, key, value, serialization=False):
        if serialization:
            self.cache.set(key, pickle.dumps(value))
        else:
            self.cache.set(key, value)

    def get(self, key, serialization=False):
        result = self.cache.get(key)
        if serialization and result is not None:
            result = pickle.loads(result)
        return result

    def delete(self, key):
        return self.cache.delete(key)

    def flush(self):
        self.cache.flushall()

    def keys(self):
        return self.cache.keys()



redis_cache = RedisCacheService(
    host=os.getenv('REDIS_CACHE_HOST'),
    port=os.getenv('REDIS_CACHE_PORT'),
    db=os.getenv('REDIS_CACHE_DB'),
    password=os.getenv('REDIS_CACHE_PASSWORD')
)

