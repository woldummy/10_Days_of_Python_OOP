# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-08-06
# macOS: 14.2.1  Python: 3.12


class MyClass:
    # Class attribute
    attribute = "This is a class attribute."

    # Initializer / Instance attributes
    def __init__(self, value):
        self.instance_attribute = value

    # Method
    def my_method(self):
        return f"My instance attribute is: {self.instance_attribute}"

if __name__ == "__main__":
    my_object = MyClass("Hello, Object!")
    print(my_object.instance_attribute) # Accessing an instance attribute
    print(my_object.my_method()) # Calling a method on the objectoo
