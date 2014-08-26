#!/usr/bin/env python3
"This is a module for Bank a/c"

class Customer:
    """Class for Customer"""
    def __init__(self, name, accounts = None):
        self.name = name
        if accounts == None:
            accounts = dict()
        self._accounts = accounts
        
    def name(self):
        """Retuns name of customer"""
        return self.name
    
    def accounts(self):
        """Prints details of acounts"""
        for ac in self._accounts:
            print("{} => Rs {}".format(ac, self._accounts[ac].balance()))
    
    def transfer(self, f, t, amount):
        """transfers money from one a/c to other
            Input:
                f: from account
                t: to account
                amount: amount to transfer
        """
        from_ac = self._accounts[f]
        to_ac = self._accounts[t]
        from_ac.transfer(to_ac, amount) 