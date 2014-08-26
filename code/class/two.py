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
 
    def withdraw(self, amount): 
        self._balance -= amount
 
    def balance(self): 
         return self._balance
