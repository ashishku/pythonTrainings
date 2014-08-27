from Customer import Customer
from Account import SavingsAccount, CurrentAccount

customer = Customer('Ashish Kumar', {'saving': SavingsAccount(100, 500), 'current': CurrentAccount(1000)})

customer.accounts()

try:
    customer.transfer('saving', 'current', 600)
    customer.accounts()
except ValueError as err:
    print("Transaction failed: " + str(err))
    
try:
    customer.transfer('current', 'saving', 600)
    customer.accounts()
except ValueError as err:
    print("Transaction failed: " + str(err))