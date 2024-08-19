# -*- coding: UTF-8 -*-
# Decorator with functools wraps which repairs introspection
# found at https://realpython.com/primer-on-python-decorators/
# 1.Run: comment out @wraps(func) and @logged decorator and run the code
# 2.Run: uncomment @logged and run the code
# 3.Run: uncomment @wraps(func) and run the code
# see how introspection is repaired
# Name: wolke
# Date: 2024-08-19
# macOS: 14.2.1  Python: 3.12

from functools import wraps


def logged(func):
    # @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

# @logged
def f(x):
    """does some math"""
    return x + x * x

if __name__ == "__main__":
    result = f(2)
    print(f"Result: {result}")  # prints '6'
    print(f"Function in use: {f.__name__}")  # prints 'f'
    print(f"Doc of function in use: {f.__doc__}")  # prints 'does some math'
