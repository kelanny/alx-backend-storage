#!/usr/bin/env python3
"""
This module contains a Cache class for interacting with a Redis database.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    A class to interact with Redis,
    providing methods to store and retrieve data.
    """

    def __init__(self):
        """
        Initialize the Cache instance and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key associated with the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


# Example usage
if __name__ == "__main__":
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
