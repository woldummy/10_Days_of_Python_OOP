# -*- coding: UTF-8 -*-
# Using Exception Hierarchies in Data Science
# this examples avoids pandas and just uses csv module
# Name: wolke
# Date: 2024-11-04
# macOS: 14.2.1  Python: 3.12


import csv

"""FileNotFoundError and PermissionError:
These exceptions are specific to file operations. Catching them first ensures we handle file access issues 
before considering more general errors. This differentiation is important for debugging and for providing 
clear feedback to the user or logs.
ValueError: 
This exception is raised if there’s an issue with the dataformat, such as when converting 
a column to a numeric type fails because the data contains non-numeric values. 
Handling this separately allows us to provide a specific message about data processing issues.
Exception: 
This is a catch-all for any other exceptions not previously caught. 
It’s placed last to ensure that specific exceptions are not masked by this more general handler.

This example illustrates how to manage exception hierarchies in a datascience context, ensuring that each step
 of the data loading and preprocessing phase is robust against potential errors. By catching more specific exceptions 
 first, we can provide targeted responses to different error conditions, improving the reliability and user-friendliness 
 of our datascience pipelines.
"""


def load_and_preprocess_data(filepath):
    try:
        # Attempt to load the data file from csv file
        with open(filepath, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        # Perform some preprocessing on the data
        for row in data:
            row['price'] = float(row['price'])  # Convert price to numeric
        # Return the preprocessed data
        return data
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read {filepath}.")
    except ValueError as e:
        print(f"Error processing file {filepath}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Test the data loading and preprocessing function
    data_file = "data.csv"
    data= load_and_preprocess_data(data_file)
    # Output:`
    print(data)