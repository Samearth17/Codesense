class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
        
    def get_balance(self):
        return self.balance