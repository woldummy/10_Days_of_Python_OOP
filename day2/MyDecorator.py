# -*- coding: UTF-8 -*-
# Ten days of Python Day 2
# showing how to use a decorator without the @ syntax
# Name: wolke
# Date: 2024-08-13
# macOS: 14.2.1  Python: 3.12

def my_decorator(func):
    def wrapper():  # The function is an inner function wrapped by the decorator
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_hello():
    print("Hello!")


if __name__ == "__main__":
    # The function is wrapped by the decorator
    say_hello = my_decorator(say_hello)  # say_hello now points to inner wrapper function
    say_hello()