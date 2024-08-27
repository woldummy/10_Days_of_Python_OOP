# -*- coding: UTF-8 -*-
# using _ for internal implementations
# Name: wolke
# Date: 2024-08-27
# macOS: 14.2.1  Python: 3.12


class MyClass:

    def __init__(self):
        self.__private_var = "This is a private variable"

    def public_method(self):
        print("This is a public method")


    def _internal_method(self):
        print("This is an internal method")
        print("Can be called from outside the class but SHOULD NOT be called.")

    def __private_method(self):
        print("This is an even more private method")
        print("Can NOT be called from outside the class without 'tricks'.")



if __name__ == "__main__":
    my_object = MyClass()
    my_object.public_method()  # Good!
    my_object._internal_method()  # Not recommended
    my_object.__private_method()  # Will not work

# In this example, _internal_method is an internal method of MyClass meant
# to be used by othermethods within the class and not directly accessed from outside the class.
