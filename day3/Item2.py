# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-08-20
# macOS: 14.2.1  Python: 3.12

from functools import total_ordering


@total_ordering
class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Item):
            # Don't attempt to compare against unrelated types
            return NotImplemented
        # first compare value than name
        return self.name == other.name and self.value == other.value


    def __gt__(self, other):
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.name > other.name:
                return True
        return False


if __name__ == "__main__":
    item1 = Item('Apple', 10)
    item2 = Item('Banana', 20)
    item3 = Item('Banana', 10)
    # Comparing the items
    print(item1 == item2)
    print(item1 != item2)
    print(item1 < item2)
    print(item1 <= item2)
    print(item1 > item2)
    print(item1 >= item2)
    # Output: False # Output: True # Output: True # Output: True # Output: False # Output: False