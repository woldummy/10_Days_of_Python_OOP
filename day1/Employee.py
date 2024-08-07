# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-08-07
# macOS: 14.2.1  Python: 3.12


class Employee:
    num_of_employees = 0 # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_employees += 1

    @classmethod
    def get_num_of_employees(cls):
        return f"Total number of employees: {cls.num_of_employees}"


# Accessing a class method without creating an instance
print(Employee.get_num_of_employees())
# Creating instances of Employee
emp1 = Employee("John", 50000)
emp2 = Employee("Doe", 60000)
# Accessing the class method after creating instances
print(Employee.get_num_of_employees())
