# -*- coding: UTF-8 -*-
# CustomDataFrame.py shows usage of __getitem__ and __setitem__
# Name: wolke
# Date: 2024-08-27
# macOS: 14.2.1  Python: 3.12


class CustomDataFrame:

    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        # Assign a new value to a specific row
        self.data[key] = value



# Example usage
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_dataframe = CustomDataFrame(data)
my_dataframe[1] = [10, 11, 12] # Modify the second row print(my_dataframe[1]) # Output: [10, 11, 12]