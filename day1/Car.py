# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-08-06
# macOS: 14.2.1  Python: 3.12


class Car:
    # Class attribute
    total_cars = 0
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1 # Increment the total number of cars each time a new car is created

    # Instance method
    def description(self):
        """Returns a description of the car."""
        return f"{self.year} {self.make} {self.model}"

    # Class method
    @classmethod
    def total_cars_created(cls):
        """Returns the total number of cars created."""
        return f"Total cars created: {cls.total_cars}"

    # Static method
    @staticmethod
    def is_vintage(year):
        """Determines if a car is vintage based on its year."""
        return year < 1990



if __name__ == "__main__":
    # Creating car objects
    car1 = Car("Toyota", "Corolla", 1985)
    car2 = Car("Ford", "Mustang", 1968)

    # Using an instance method
    print(car1.description())  # Output: 1985 Toyota Corolla print(car2.description()) # Output: 1968 Ford Mustang

    # Using a class method
    print(Car.total_cars_created())  # Output: Total cars created: 2
    # Using a static method
    print(Car.is_vintage(1985)) # Output: True
    print(Car.is_vintage(1995)) # Output: False
