# -*- coding: UTF-8 -*-
# Class Method Polymorphism
# Name: wolke
# Date: 2024-10-22
# macOS: 14.2.1  Python: 3.12

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


def animal_sound(animal: Animal):
    print(animal.speak())

if __name__ == "__main__":
    # Polymorphism in action
    dog = Dog()
    cat = Cat()
    animal_sound(dog)  # Output: Woof!
    animal_sound(cat) # Output: Meow!