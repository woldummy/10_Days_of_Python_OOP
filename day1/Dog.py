# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-08-06
# macOS: 14.2.1  Python: 3.12


class Dog:
    species = "Canis familiaris" # Class attribute

    def __init__(self, name, age):
        self.name = name # Instance attribute self.age = age # Instance attribute


if __name__ == "__main__":
    # Accessing a class attribute
    print(Dog.species) # Output: Canis familiaris

    # Class attributes are shared by all instances
    dog1 = Dog("Buddy", 5)
    dog2 = Dog("Molly", 3)
    print(f"{dog1.name} belongs to {Dog.species}")  # Output: Canis familiaris
    Dog.species = "Canis lupus"  # Changing the class attribute
    print(f"{dog2.name} belongs to {dog2.species}")  # Output: Canis familiaris
    print(f"{dog1.name} belongs to {Dog.species}")  # Output: Canis familiaris
