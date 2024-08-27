# -*- coding: UTF-8 -*-
# DataCollection.py shows __next__ and __iter__
# Name: wolke
# Date: 2024-08-27
# macOS: 14.2.1  Python: 3.12


class DataCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Example usage
data = [1, 2, 3, 4, 5]
collection = DataCollection(data)
for item in collection:
        print(item) # Outputs each item in data
