# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-08-13
# macOS: 14.2.1  Python: 3.12


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_as_string: str) -> Date:
        year, month, day = map(int, date_as_string.split('-'))
        return cls(year, month, day) # Creating a new instance using the class method

if __name__ == "__main__":
    # Default constructor
    date1 = Date(2024, 3, 2) # Alternative constructor
    date2 = Date.from_string("2024-03-02")
    print(f"Date1: {date1.year}-{date1.month}-{date1.day}")
    print(f"Date2: {date2.year}-{date2.month}-{date2.day}")
