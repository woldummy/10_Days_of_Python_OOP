# -*- coding: UTF-8 -*-
# showing how to use a decorator with *args and **kwargs
# 2 examples: add and better_add
# Name: wolke
# Date: 2024-08-18
# macOS: 14.2.1  Python: 3.12


def add_decorator(func):
    def wrapper(a, b):
        print(f"Something is happening before the function <{func.__name__}> is called.")
        val = func(a, b)
        return val
    return wrapper


def add_better_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Something is happening before the function <{func.__name__}> is called.")
        val = func(*args)
        return val
    return wrapper


@add_decorator
def add(a, b):
    return a + b


@add_better_decorator
def better_add(*args):  # *args, *kwargs
    sum = 0
    for arg in args:
        sum += arg
    return sum


if __name__ == "__main__":
    # The functions are wrapped by the decorator
    # print(add(1, 2))
    print(better_add(1, 2, 3, 4, 5))
    print(better_add.__name__)
