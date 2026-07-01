class Account:
    def __init__(self, name, balance):
        # instance attributes
        self.name = name
        self.balance = balance
    
    # method to withdraw money from account
    def withdraw(self, amount):
        # check if amount is a valid number
        if not isinstance(amount, (int, float)):
            raise ValueError('Invalid amount')
        
        # check if amount is greater than balance
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        
        # subtract the amount from the balance
        self.balance -= amount
    
    # method to deposit money to account
    def deposit(self, amount):
        # check if amount is a valid number
        if not isinstance(amount, (int, float)):
            raise ValueError('Invalid amount')
        
        # add the amount to the balance
        self.balance +=amount

# create an instance of the Account class
my_account = Account('John Doe', 100)

# withdraw money from account
my_account.withdraw(50)

# deposit money to account
my_account.deposit(20)

# print the updated balance
print('Account balance:', my_account.balance)