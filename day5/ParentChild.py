# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-09-03
# macOS: 14.2.1  Python: 3.12

class Parent:
    def __init__(self, value):
        self.value = value
        print(f"Parent class with value: {self.value}")

class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value) # Calling Parent class __init__
        self.extra = extra
        print(f"Child class with value: {self.value} and extra: {self.extra}")

# Creating an instance of Child
child_instance = Child(10, 20)