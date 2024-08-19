# -*- coding: UTF-8 -*-
# Day 2 of Ten Days of Python / Aidditional Python Features
# found at https://realpython.com/primer-on-python-decorators/
# Name: wolke
# Date: 2024-08-13
# macOS: 14.2.1  Python: 3.12
import functools
import time

# To fix introspection, decorators should use the @functools.wraps decorator,
# which will preserve information about the original function.

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])

waste_some_time(1)
waste_some_time(999)

# The @functools.wraps decorator uses the function functools.update_wrapper()
# to update special attributes like __name__ and __doc__.
print(waste_some_time.__name__)
help(waste_some_time)
