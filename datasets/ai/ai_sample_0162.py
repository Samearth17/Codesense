# account class with the necessary functions 
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

# ATM class with the necessary functions
class ATM:
    def __init__(self):
        self.accounts = []

    def createAccount(self, name, balance):
        account = Account(name, balance)
        self.accounts.append(account)

    def deposit(self, name, amount):
        for account in self.accounts:
            if account.name == name:
                account.deposit(amount)

    def withdrawal(self, name, amount):
        for account in self.accounts:
            if account.name == name:
                account.withdrawal(amount)

    def printBalance(self, name):
        for account in self.accounts:
            if account.name == name:
                print(name, " Balance: ", account.balance)