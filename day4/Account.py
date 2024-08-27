# -*- coding: UTF-8 -*-
# Account class with usage of private attributes
# Name: wolke
# Date: 2024-08-27
# macOS: 14.2.1  Python: 3.12

# add __str__, __repr__, __eq__, __lt__ .... methods

class Account:
    def __init__(self, balance: float):
        self.__balance = balance # Name mangling to make it harder to access directly

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount # Accessing the mangled name internally

    def withdraw(self, amount) -> float:
        if 0 < amount <= self.__balance:
            self.__balance -= amount

account = Account(100)

# Direct access to '__balance' would fail; Python mangles the name to '_Account__balance'.
