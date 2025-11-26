# 5.	Design a banking system with:
# •	An abstract base class Account with deposit(), withdraw(), calculate_interest().
# •	Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# •	Each account must:
# o	Encapsulate balance (private)
# o	Provide controlled access through properties
# o	Override interest calculation differently
# •	Include a static method to validate amount.
# •	Include a class method to update bank-wide interest policies.

from abc import ABC, abstractmethod

class Account(ABC):
    intrest=0.02
    def __init__(self,b):
        self.__balance=b
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance+=amount
    def calender_intrest(self):
        self.__balannce+=self.__balance*self.intrest
    def get_balance(self):
        return self.__balance
    def set_balance(self,nb):
        self.__balance=nb

class SA(Account):
    pass
class CA(Account):
    pass
