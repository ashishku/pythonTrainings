#!/usr/bin/env python3
"This is a module for Bank a/c"

class Customer:
    def __init__(self, name, accounts = None):
        self.name = name
        if accounts == None:
            accounts = dict()
        self._accounts = accounts
        
    def name(self):
        return self.name
    
    def accounts(self):
        for ac in self._accounts:
            print("{} => Rs {}".format(ac, self._accounts[ac].balance()))
    
    def transfer(self, f, t, amount):
        from_ac = self._accounts[f]
        to_ac = self._accounts[t]
        from_ac.transfer(to_ac, amount)

class Account:
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
    def __init__(self, minbalance, balance):
        super().__init__(balance)
        self._min_balance = minbalance
 
    def withdraw(self, amount):
        if  self._balance - amount < self._min_balance:
            raise ValueError("Cannot have less than Rs {} balance".format(self._min_balance))
        self._balance -= amount
 
class CurrentAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount): 
        self._balance -= amount
 