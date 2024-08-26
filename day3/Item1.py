# -*- coding: UTF-8 -*-
# explainig the __eq__ method
# Name: wolke
# Date: 2024-08-20
# macOS: 14.2.1  Python: 3.12


class Item:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Item):
            # Don't attempt to compare against unrelated types
            return NotImplemented
        return self.name == other.name   # also see hashing

if __name__ == "__main__":
    item1 = Item('Apple')
    item2 = Item('Apple')
    item3 = Item('Banana')
    print(item1 == item2) # Output: True, because their names are the same
    print(item1 == item3) # Output: False, because their names are different