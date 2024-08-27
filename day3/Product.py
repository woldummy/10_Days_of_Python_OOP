# -*- coding: UTF-8 -*-
# Example of __str__ and __repr__ methods
# Name: wolke
# Date: 2024-08-20
# macOS: 14.2.1  Python: 3.12

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}) - User Friendly"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

if __name__ == "__main__":
    # Creating an instance of Product
    product = Product('Coffee', 5.99)
    # Using print() or str() calls __str__()
    print(product)  # Output: Product(name=Coffee, price=5.99) - User Friendly # Using repr() or printing in the console calls __repr__()
    print(repr(product))  # Output: Product('Coffee', 5.99)
    p = Product('Coffee', 4.99)
