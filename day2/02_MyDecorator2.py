# -*- coding: UTF-8 -*-
# Ten days of Python Day 2
# showing how to use a decorator the @ syntax
# Name: wolke
# Date: 2024-08-13
# macOS: 14.2.1  Python: 3.12


def my_decorator(func):
    def wrapper(name):
        print("Something is happening before the function is called.")
        func(name)
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # The function is wrapped by the decorator
    say_hello("Alice")
    print(say_hello.__name__)
