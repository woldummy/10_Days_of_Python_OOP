# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-10-22
# macOS: 14.2.1  Python: 3.12

# In many programming languages, method overloading refers to the ability to
# have multiple methods with the same name but different parameters.
# DOES NOT EXIST IN PYTHON
# i.e. Java:
# static int plusMethod(int x, int y) {
#   return x + y;
# }
#
# static double plusMethod(double x, double y) {
#   return x + y;
# }

# but
def greet(name="Guest"):
    '''First example of method overloading in Python'''
    print(f"Hello, {name}!")


def create_user(name, age, email, country="Unknown"):
    """Second example of method overloading in Python.
        Named arguments make it possible to have 'multiple'
        functions with the same name but different parameters.
     Better: Clarity,Flexibility, Order Independence"""
    return {'name': name, 'age': age, 'email': email, 'country': country}



if __name__ == "__main__":
    greet()  # Output: Hello, Guest! print(f"Hello, {name}!")
    greet("Alice")  # Output: Hello, Alice!
    user_info = create_user(name="John Doe", email="john@example.com", age=30)
    user_info2 = create_user(name="John Doe", email="john@example.com", age=30, country="USA")

    print(user_info)  # Output: {'name': 'John Doe', 'age': 30, 'email': '
    print(user_info2)  # Output: {'name': 'John Doe', 'age': 30, 'email': '