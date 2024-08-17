# -*- coding: UTF-8 -*-
# Ten days of Python Day 2
# Name: wolke
# Date: 2024-08-13
# macOS: 14.2.1  Python: 3.12
from time import sleep


def memoize(func):
    cache = {}
    def memoized_func(*args):
        if args in cache:
            print(f"Fetching cached result for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"Caching result for {args}")
        return result
    return memoized_func

@memoize
def expensive_computation(x, y):
# Simulating an expensive computation, e.g., a complex data transformation from time import sleep
    sleep(2) # Simulating time-consuming computation
    return x * y + x - y

# Using the decorated function
print(expensive_computation(5, 10))
print(expensive_computation(5, 10)) # This will fetch the result from the cache