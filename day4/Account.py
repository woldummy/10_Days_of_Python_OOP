# -*- coding: UTF-8 -*-
# Account class with usage of private attributes
# Name: wolke
# Date: 2024-08-27
# macOS: 14.2.1  Python: 3.12
# add __str__, __repr__, __eq__, __lt__ , .... methods

from functools import total_ordering

@total_ordering
class Account:
    def __init__(self, balance: float):
        self.__balance = balance # Name mangling to make it harder to access directly

    def __str__(self):
        return f"Account with balance: {self.__balance}"

    def __repr__(self):
        return f"Account({self.__balance})"

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount # Accessing the mangled name internally

    def __eq__(self, other):
        if not isinstance(other, Account):
            # Don't attempt to compare against unrelated types
            return NotImplemented
        return self.__balance == other.__balance

    def __gt__(self, other):
        if self.__balance > other.__balance:
            return True
        return False

    def withdraw(self, amount) -> float:
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")


if __name__ == "__main__":
    account = Account(100)
    account1 = Account(100)
    # account1.deposit(300)
    account2 = Account(200)
    print(account == account1)  # Output: True
    print(account == account2)  # Output: False
    print(account2 >= account)  # Output: True
    print(account)  # Output: Account balance: 100
    print(repr(account))  # Output: Account(100)

    # Direct access  to '__balance' would fail;
    # Python mangles the name to '_Account__balance'.
