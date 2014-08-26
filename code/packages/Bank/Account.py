#!/usr/bin/env python3
"This is a module for Bank a/c"

class Account:
    """Abstract class for A/c"""
    def __init__(self, balance):        
        self._balance = balance
        
    def transfer(self, target, amount): 
        self.withdraw(amount)
        target.deposit(amount)
 
    def deposit(self, amount): 
        self._balance += amount 
 
    def balance(self): 
         return self._balance

class SavingsAccount(Account):
    """a saving bank a/c.
       must have the minmum balance maintained
    """
    def __init__(self, minbalance, balance):
        super().__init__(balance)
        self._min_balance = minbalance
 
    def withdraw(self, amount):
        """Widraw money from a/c
           Raies: Value Error for -ve balance 
        """
        if  self._balance - amount < self._min_balance:
            raise ValueError("Cannot have less than Rs {} balance".format(self._min_balance))
        self._balance -= amount
 
class CurrentAccount(Account):
    """a current a/c.
       can have -ve balance
    """
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        """Widraw money from a/c""" 
        self._balance -= amount
 