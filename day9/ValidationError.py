# -*- coding: UTF-8 -*-
# First example of using a custom exception class named ValidationError
# Name: wolke
# Date: 2024-11-04
# macOS: 14.2.1  Python: 3.12

class ValidationError(Exception):
    """Exception raised for errors in the input validation.

    Attributes:
        message -- explanation of the error
        value -- input value which caused the error
    """

    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(message)


def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative", age)
    elif age < 18:
        raise ValidationError("You must be at least 18 years old", age)
    else:
        print("Age is valid")


# Example usage
try:
    validate_age(-1)
except ValidationError as e:
    print(f"Error: {e.message} - Invalid Value: {e.value}")