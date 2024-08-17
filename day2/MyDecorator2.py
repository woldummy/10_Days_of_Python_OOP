# -*- coding: UTF-8 -*-
# Ten days of Python Day 2
# Name: wolke
# Date: 2024-08-13
# macOS: 14.2.1  Python: 3.12


def my_decorator(func):
    def wrapper(name):
        print("Something is happening before the function is called.")
        func(name)
        print("Something is happening after the function is called.")
    return wrapper

def add_decorator(func):
    def wrapper(a, b):
        print("Something is happening before the function is called.")
        return func(a, b)
        # print("Something is happening after the function is called.")
    return wrapper


@add_decorator
def add(a, b):
    return a + b

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # The function is wrapped by the decorator
    # say_hello("Alice")
    print(add(1, 2))
