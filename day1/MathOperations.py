# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-08-07
# macOS: 14.2.1  Python: 3.12


class MathOperations:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Using static methods without creating an instance of the class
print(MathOperations.add(5, 7)) # Output: 12
print(MathOperations.multiply(3, 4)) # Output: 12