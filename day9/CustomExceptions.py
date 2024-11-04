# -*- coding: UTF-8 -*-
# Create Custom Exceptions and Use Them in Python
# Name: wolke
# Date: 2024-11-04
# macOS: 14.2.1  Python: 3.12

# Benefits of custom exceptions
"""
- Clarity and Maintainability: Using a well-defined exception hierarchy
  makes your code clearer and easier to maintain. Other developers (or you
  in the future) can quickly understand the kinds of errors your code can
  raise and how they are related.
- Robustness: It enables more robust error handling by allowing you to
  catch and handle specific errors differently, providing more precise
  reactions to different failure conditions.
- Best Practices: This approach aligns with Python’s philosophy and best
  practices for exception handling, ensuring that your code is idiomatic
  and Pythonic.

Custom exceptions are a powerful feature in Python that can greatly
enhance the readability, maintainability, and robustness of your
application’s error handling. By defining your own exceptions, you can
create a more intuitive and fine-grained error handling mechanism that is
tailored to the specific requirements of your application. Remember to
inherit from the Exception class or one of its subclasses and leverage the full
potential of Python's exception handling capabilities.
"""

# Scenario: Data Validation for a Machine Learning Model
"""
Imagine you’re preparing data for a machine learning model that predicts
house prices. The dataset includes features like the number of bedrooms,
square footage, and the year the house was built. Before training the model,
you need to validate that the data meets certain criteria, such as:
- The number of bedrooms must be a positive integer.
- The square footage must be within a reasonable range.
- The year the house was built must not be in the future.

To handle violations of these criteria, you’ll define custom exceptions.
"""

# Step 1: Define Custom Exceptions
class DataValidationError(Exception):
    """Base class for exceptions in data validation."""
    pass

class BedroomCountError(DataValidationError):
    """Exception raised for errors in the number of bedrooms."""
    pass

class SquareFootageError(DataValidationError):
    """Exception raised for errors in the square footage."""
    pass

class YearBuiltError(DataValidationError):
    """Exception raised for errors in the year the house was built."""
    pass

# Step 2: Implement Data Validation Functions
def validate_house_data(house):
    if not isinstance(house['bedrooms'], int) or house['bedrooms'] <= 0:
        raise BedroomCountError(f"Invalid number of bedrooms: {house['bedrooms']}")
    if house['square_footage'] < 100 or house['square_footage'] > 10000:
        raise SquareFootageError(f"Square footage out of range: {house['square_footage']}")
    from datetime import datetime
    if house['year_built'] > datetime.now().year:
        raise YearBuiltError(f"Year built is in the future: {house['year_built']}")
    print("House data is valid.")

# Step 3: Test the Data Validation Functions
# Valid house data
house1 = {'bedrooms': 3, 'square_footage': 1500, 'year_built': 1990}
house2 = {'bedrooms': 0, 'square_footage': 1500, 'year_built': 1990}
try:
    validate_house_data(house1)
    validate_house_data(house2)
except DataValidationError as e:
    print(f"Data validation error: {e}")